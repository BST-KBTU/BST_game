import pygame, sys
import numpy as np
import random
from dijkstra import find
from char import  *
from maze_pacman import  *
from database import get_best, cur, insert_result
pygame.init()

screen = pygame.display.set_mode((Width,Height))
pm_size = 20
# caption and icon 
pygame.display.set_caption("PacMan")
pygame.display.set_icon(logo)
timer = pygame.time.Clock()

coin = []
lives = [1 ,1 ,1]

High_score = get_best()

for score in enumerate(High_score):
		h_score= score[1]
		s = f"{h_score}"

def draw_text(words, screen, pos, size, color, font_name, centered=False):
	font = pygame.font.SysFont(font_name, size)
	text = font.render(words, False, color)
	screen.blit(text,pos)

def get_index(x,y):
	index_x = x//20
	index_y = y//20
	return index_x, index_y

def menu():
	pygame.mixer.init()
	pygame.mixer.music.load('intro.mp3')
	pygame.mixer.music.play(-1, 0.0)

	while True:
		screen.fill((Yellow))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pygame.mixer.music.stop()
					game()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LSHIFT:
					second_page()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_f:
					F()

		screen.blit(logo1, (120, 20))
		draw_text('MAIN MENU', screen, [240, 110], 16, Black, Font)
		draw_text('PRESS SHIFT', screen, [180, 340], 32, White, Font)
		draw_text('TO KNOW MORE', screen, [230, 380], 16, White, Font)
		draw_text('PRESS             TO START', screen, [90, 220], 32, Black, Font)
		draw_text('SPACE', screen, [220, 220], 32, Red, Font)
		draw_text('PRESS F TO PAY RESPECT', screen, [10, 600], 12, White, Font)
		pygame.display.update()
		timer.tick(1)

def second_page():
	while True:
		screen.fill((Blue))
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					menu()
		screen.blit(bghost1, (40, 220))
		screen.blit(bghost2, (40, 320))
		screen.blit(bghost3, (40, 420))
		screen.blit(bghost4, (40, 520))
		screen.blit(bpacman, (40, 120))

		draw_text('CHARACTERS', screen, [180, 40], 32, White, Font)
		draw_text('PACMAN', screen, [120, 130], 24, White, Font)
		draw_text('GOHA', screen, [120, 230], 24, White, Font)
		draw_text('PINKY', screen, [120, 330], 24, White, Font)
		draw_text('TINKY', screen, [120, 430], 24, White, Font)
		draw_text('WINKY', screen, [120, 530], 24, White, Font)
		pygame.display.update()

def F():
	while True:
		screen.blit(cute, (0, 0))
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					menu()
		pygame.display.update()

def close():
	while True:
		screen.fill((Black))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit()
				sys.exit()
		screen.blit(f1, (20, 100))
		screen.blit(f1, (200, 400))
		screen.blit(f1, (300, 200))
		screen.blit(logo1, (120, 20))
		screen.blit(ghost5, (250, 350))
		screen.blit(hat, (260, 280))

		draw_text('FINISH', screen, [233, 140], 32, White, Font)
		draw_text('YOU WON', screen, [208, 240], 32, White, Font) 
		pygame.display.update()
		timer.tick(1)

def lose():
	while True:
		screen.fill((Black))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					menu()
		
		screen.blit(logo1, (120, 20))
		screen.blit(ghost5, (250, 300))
		draw_text('FINISH', screen, [233, 140], 32, White, Font)
		draw_text('YOU LOSE', screen, [208, 240], 32, White, Font)
		draw_text('LAME LOOSER', screen, [180, 440], 32, White, Font)
		pygame.display.update()			 
		timer.tick(1) 
        
class Enemy():
	x = 0
	y = 0
	goal_x = None
	goal_y = None
	def __init__(self):
		global pm_maze
		self.x = None
		self.y = None
		self.goal_x = None
		self.goal_y = None
		while self.x is None or pm_maze[self.y][self.x] != 5:
			self.x = random.randint(0,len(pm_maze[0])-1)
			self.y = random.randint(0,len(pm_maze)-1)

	def find_new_goal(self):
		global pm_maze
		while self.goal_x is None or pm_maze[self.goal_y][self.goal_x] not in [1, 3, 4] or (self.goal_x == self.x and self.goal_y == self.y):
			self.goal_x = random.randint(0,len(pm_maze[0])-1)
			self.goal_y = random.randint(0,len(pm_maze)-1)

	def get_coords(self):
		return self.x, self.y

	def move(self):
		if self.goal_x is None or self.goal_x == self.x and self.goal_y == self.y:
			self.find_new_goal()
		next_x, next_y = find(pm_maze,self.x, self.y, self.goal_x, self.goal_y)
		if next_x is not None:
			self.x, self.y = next_x, next_y


class Enemy1():
	x = 0
	y = 0
	goal_x = None
	goal_y = None
	
	def __init__(self):
		global pm_maze
		self.x = None
		self.y = None
		self.goal_x = None
		self.goal_y = None
		while self.x is None or pm_maze[self.y][self.x] != 5:
			self.x = random.randint(0,len(pm_maze[0])-1)
			self.y = random.randint(0,len(pm_maze)-1)

	def find_new_goal(self, dest_x, dest_y):
		global pm_maze
		z,t = get_index(dest_x, dest_y)

		while self.goal_x is None or pm_maze[self.goal_y][self.goal_x] not in [1, 3, 4] or (self.goal_x == self.x and self.goal_y == self.y):
			self.goal_x = z
			self.goal_y = t

	def get_coords(self):
		return self.x, self.y

	def move(self, dest_x, dest_y):
		if self.goal_x is None or self.goal_x == self.x and self.goal_y == self.y:
			self.find_new_goal(dest_x, dest_y)
		tmp_x, tmp_y = get_index(dest_x, dest_y)
		next_x, next_y = find(pm_maze,self.x, self.y, tmp_x, tmp_y)
		if next_x is not None:
			self.x, self.y = next_x, next_y

enemies1 = []
enemies2 = []
enemies3 = []
enemies4 = []

enemies1.append(Enemy1())
enemies2.append(Enemy())
enemies3.append(Enemy())
enemies4.append(Enemy())

snd1 = pygame.mixer.Sound("wap1.wav")
snd2 = pygame.mixer.Sound("ahh1.wav")

def game():
#Game loop 
	global dx, dy, dt, x, y, pm_open_left, pm_open, pm_open_down, pm_open_left, pm_open_up, block, logo, background, ghost, ghost2, look_open_up, look_open_down, look_open_left
	
	snd1.play(-1)

	while True:

		for enemy in enemies1:
			enemy.move(x, y)
		for enemy in enemies2:
			enemy.move()
		for enemy in enemies3:
			enemy.move()
		for enemy in enemies4:
			enemy.move()

		save_x, save_y = x, y 

		y = y + dy
		rect1 = pygame.Rect(x, y, pm_size, pm_size)
		collide = False
		for i in range(len(pm_maze)):
			for j in range(len(pm_maze[i])):
				if pm_maze[i][j] == 0 or pm_maze[i][j] == 5:
					rect2 = pygame.Rect(j*pm_size, i*pm_size, pm_size, pm_size)
					if rect1.colliderect(rect2):
						collide = True

		if collide:
			y = save_y
			dy = 0

		x = x+dx

		rect1 = pygame.Rect(x,y,pm_size,pm_size)
		collide = False
		for i in range(len(pm_maze)):
			for j in range(len(pm_maze[i])):
				if pm_maze[i][j] == 0 or pm_maze[i][j] == 5:
					rect2 = pygame.Rect(j*pm_size,i*pm_size,pm_size,pm_size)
					if rect1.colliderect(rect2):
						collide = True

		if collide:
			x = save_x
			dx = 0

		for enemy in enemies1:
			in_x, in_y = get_index(x,y)
			if enemy.get_coords() == (in_x,in_y) or enemy.get_coords() == (in_x-1, in_y) or enemy.get_coords() == (in_x, in_y-1):
				print('end game')
				lives.pop(0)
				x = 40
				y = 100
				dx = 0
				dy = 0
				snd2.play()

		for enemy in enemies2:
			in_x, in_y = get_index(x,y)
			if enemy.get_coords() == (in_x,in_y) or enemy.get_coords() == (in_x-1, in_y) or enemy.get_coords() == (in_x, in_y-1):
				print('end game')
				lives.pop(0)
				x = 40
				y = 100
				dx = 0
				dy = 0
				snd2.play()

		for enemy in enemies3:
			in_x, in_y = get_index(x,y)
			if enemy.get_coords() == (in_x,in_y) or enemy.get_coords() == (in_x-1, in_y) or enemy.get_coords() == (in_x, in_y-1):
				print('end game')
				lives.pop(0)
				x = 40
				y = 100
				dx = 0
				dy = 0
				snd2.play()

		for enemy in enemies4:
			in_x, in_y = get_index(x,y)
			if enemy.get_coords() == (in_x,in_y) or enemy.get_coords() == (in_x-1, in_y) or enemy.get_coords() == (in_x, in_y-1):
				print('end game')
				lives.pop(0)
				x = 40
				y = 100
				dx = 0
				dy = 0
				snd2.play()

		if len((lives)) == 0:
			snd1.stop()
			pygame.mixer.init()
			pygame.mixer.music.load('ahh.mp3')
			pygame.mixer.music.play(1, 0.0)
			lose()
		
		########################################Eating coins#########################################			
		rect1 = pygame.Rect(x,y,pm_size,pm_size)
		intersect = False
		for i in range(len(pm_maze)):
			for j in range(len(pm_maze[i])):
				if pm_maze[i][j] == 1:
					coin3 = pygame.Rect(j*pm_size,i*pm_size,pm_size,pm_size)
					if rect1.colliderect(coin3):
						intersect = True
						pm_maze[i][j] = 3
						if pm_maze[i][j] == 3:
							coin.append(10)

		rect1 = pygame.Rect(x,y,pm_size,pm_size)
		intersect = False
		for i in range(len(pm_maze)):
			for j in range(len(pm_maze[i])):
				if pm_maze[i][j] == 4:
					coin3 = pygame.Rect(j*pm_size,i*pm_size,pm_size,pm_size)
					if rect1.colliderect(coin3):
						intersect = True
						pm_maze[i][j] = 3
						if pm_maze[i][j] == 3:
							coin.append(100)
		# score 					
		summ = -10
		for i in coin:
			summ += i

		
		
		#####################################Teleportation###################################
		transport = False
		rect1 = pygame.Rect(x,y,pm_size,pm_size)
		for i in range(len(pm_maze)):
			for j in range(len(pm_maze[i])):
				if pm_maze[i][j] == 6:
					trans = pygame.Rect(j*pm_size,i*pm_size,pm_size,pm_size)
					if rect1.colliderect(trans):
						transport = True

		if transport:
			x = x + 580

		transport = False
		rect1 = pygame.Rect(x,y,pm_size,pm_size)
		for i in range(len(pm_maze)):
			for j in range(len(pm_maze[i])):
				if pm_maze[i][j] == 7:
					trans = pygame.Rect(j*pm_size,i*pm_size,pm_size,pm_size)
					if rect1.colliderect(trans):
						transport = True

		if transport:
			x = x - 600

		screen.fill(Black)
	###########################################Pacman movement#####################################
		
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				quit()

			elif event.type == pygame.KEYDOWN:

				if event.key == pygame.K_UP:
					j_pac,i_pac = get_index(x, y-20)
					if pm_maze[i_pac][j_pac] in [1, 3, 4]:
						dx = 0
						dy = -20
						look_open_up = True
						look_open_left = False
						look_open_down = False
				elif event.key == pygame.K_DOWN:
					j_pac,i_pac = get_index(x, y+20)
					if pm_maze[i_pac][j_pac] in [1, 3, 4]:
						dx = 0
						dy = 20
						look_open_down = True
						look_open_left = False
						look_open_up = False
				elif event.key == pygame.K_LEFT:
					j_pac,i_pac = get_index(x-20, y)
					if pm_maze[i_pac][j_pac] in [1, 3, 4]:
						dx = -20
						dy = 0
						look_open_left = True
						look_open_up = False
						look_open_down = False
				elif event.key == pygame.K_RIGHT:
					j_pac, i_pac = get_index(x+20, y)
					if pm_maze[i_pac][j_pac] in [1, 3, 4]:
						dx = 20
						dy = 0
						look_open_left = False
						look_open_up = False
						look_open_down = False


		for i in range(len(pm_maze)):
			for j in range(len(pm_maze[i])):
				if pm_maze[i][j] == 0:
					screen.blit(block,(j*pm_size,i*pm_size))
				if pm_maze[i][j] == 1:
					pygame.draw.circle(screen, Yellow, (j*pm_size+10, i*pm_size+10), 3)
				if pm_maze[i][j] == 3:
					pygame.draw.circle(screen, Black, (j*pm_size+10, i*pm_size+10), 5)
				if pm_maze[i][j] == 4:
					pygame.draw.circle(screen, Pink, (j*pm_size+10, i*pm_size+10), 5)

		if look_open_left:		
			screen.blit(pm_open_left,(x,y))
		elif look_open_down:
			screen.blit(pm_open_down,(x,y))
		elif look_open_up:
			screen.blit(pm_open_up,(x,y))
		else:
			screen.blit(pm_open,(x,y))

		for enemy in enemies1:
			screen.blit(ghost1, (enemy.x * pm_size, enemy.y * pm_size))
		for enemy in enemies2:
			screen.blit(ghost2, (enemy.x * pm_size, enemy.y * pm_size))
		for enemy in enemies3:
			screen.blit(ghost3, (enemy.x * pm_size, enemy.y * pm_size))
		for enemy in enemies4:
			screen.blit(ghost4, (enemy.x * pm_size, enemy.y * pm_size))

		if summ == 3530:
			close()

		draw_text('Current Score: {}'.format(summ),screen, [120,0], 16, White, Font)
		draw_text('High Score:',screen, [320,0], 16, White, Font)
		draw_text(s[1:5],screen,[440,0],16,White,Font)
		screen.blit(pm_open, (10 ,645))
		screen.blit(pm_open, (30 ,645))
		screen.blit(pm_open, (50 ,645))
		if len((lives)) == 2:
			pygame.draw.circle(screen, Black, (60, 655), 10)
		if len((lives)) == 1:
			pygame.draw.circle(screen, Black, (60, 655), 10)
			pygame.draw.circle(screen, Black, (40, 655), 10)

		pygame.display.flip()
		timer.tick(FPS)
		insert_result(summ)
	pygame.display.update()

menu()
