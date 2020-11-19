import pygame, sys
import numpy as np
import random
from dijkstra import find
from char import  *  # * - same folder
from maze_pacman import  *
vec = pygame.math.Vector2
pygame.init()

screen = pygame.display.set_mode((Width,Height))
pm_size = 20
# caption and icon 
pygame.display.set_caption("PacMan")
pygame.display.set_icon(logo)
timer = pygame.time.Clock()

coin = []
scores = []
scores_maximum = []

def draw_text(words, screen, pos, size, color, font_name, centered=False):
	font = pygame.font.SysFont(font_name, size)
	text = font.render(words, False, color)
	screen.blit(text,pos)


def get_index_map_by_coord(x,y):
	index_x = x//20
	index_y = y//20
	return index_x, index_y


def menu():
	#pygame.mixer.init()
	#pygame.mixer.music.load('intro.mp3')
	#pygame.mixer.music.play(-1, 0.0)

	while True:
		screen.fill((Yellow))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					game()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LSHIFT:
					second_page()
		#button = pygame.Rect(50, 100, 200, 50)
		#pygame.draw.rect(screen, (255, 0, 0), button)
		screen.blit(logo1, (120, 20))
		#draw_text('PRESS SPACE', screen, [50, 100], 20, White, Font)
		draw_text('MAIN MENU', screen, [190, 140], 32, White, Font)
		draw_text('PRESS SHIFT', screen, [180, 240], 32, White, Font)
		draw_text('PRESS SPACE TO START', screen, [90, 340], 32, White, Font)
		draw_text('PRESS F TO PAY RESPECT', screen, [10, 600], 12, White, Font)
		pygame.display.update()
		timer.tick(1)

def second_page():
	while True:
		screen.fill((Black))
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					menu()
		draw_text('MAIN MENU', screen, [190, 140], 32, White, Font)
		draw_text('PRESS SHIFT', screen, [180, 240], 32, White, Font)
		pygame.display.update()


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
		print("chosen start position", self.x, self.y)

	def find_new_goal(self):
		global pm_maze
		while self.goal_x is None or pm_maze[self.goal_y][self.goal_x] not in [1,4] or (self.goal_x == self.x and self.goal_y == self.y):
			self.goal_x = random.randint(0,len(pm_maze[0])-1)
			self.goal_y = random.randint(0,len(pm_maze)-1)
		print("chosen new goal", self.goal_x, self.goal_y, "there we have", pm_maze[self.goal_y][self.goal_x])

	def get_coords(self):
		return self.x*20, self.y*20

	def move(self):
		if self.goal_x is None or self.goal_x == self.x and self.goal_y == self.y:
			self.find_new_goal()
		next_x, next_y = find(pm_maze,self.x, self.y, self.goal_x, self.goal_y)
		if next_x is not None:
			self.x, self.y = next_x, next_y


enemies1 = []
enemies2 = []
enemies3 = []
enemies4 = []

enemies1.append(Enemy())
enemies2.append(Enemy())
enemies3.append(Enemy())
enemies4.append(Enemy())
# enemies.append(Enemy())


def game():
#Game loop 
	global a, b, da, db, z, t, dz, dx, dy, dt, x, y, pm_open_left, pm_open, pm_open_down, pm_open_left, pm_open_up, block, logo, background, ghost, ghost2, look_open_up, look_open_down, look_open_left
	
	#pygame.mixer.init()
	#pygame.mixer.music.load('wap.mp3')
	#pygame.mixer.music.play(-1, 0.0)
	
	while True:

		for enemy in enemies1:
			enemy.move()
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


		"""for enemy in enemies:
			print((rect1.x, rect1.y),enemy.get_coords())
			if enemy.get_coords() == (rect1.x, rect1.y):
				print('end game')"""


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

		#scores.append(summ)
		#scores_max = np.max(scores)
		
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
					j_pac,i_pac = get_index_map_by_coord(x, y-20)
					if pm_maze[i_pac][j_pac] in [1, 3, 4]:
						dx = 0
						dy = -20
						look_open_up = True
						look_open_left = False
						look_open_down = False
				elif event.key == pygame.K_DOWN:
					j_pac,i_pac = get_index_map_by_coord(x, y+20)
					if pm_maze[i_pac][j_pac] in [1, 3, 4]:
						dx = 0
						dy = 20
						look_open_down = True
						look_open_left = False
						look_open_up = False
				elif event.key == pygame.K_LEFT:
					j_pac,i_pac = get_index_map_by_coord(x-20, y)
					if pm_maze[i_pac][j_pac] in [1, 3, 4]:
						dx = -20
						dy = 0
						look_open_left = True
						look_open_up = False
						look_open_down = False
				elif event.key == pygame.K_RIGHT:
					j_pac, i_pac = get_index_map_by_coord(x+20, y)
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
		
		# screen.blit(ghost1, (z, t))
		# screen.blit(ghost2, (a, b))

		for enemy in enemies1:
			screen.blit(ghost1, (enemy.x * pm_size, enemy.y * pm_size))
		for enemy in enemies2:
			screen.blit(ghost2, (enemy.x * pm_size, enemy.y * pm_size))
		for enemy in enemies3:
			screen.blit(ghost3, (enemy.x * pm_size, enemy.y * pm_size))
		for enemy in enemies4:
			screen.blit(ghost4, (enemy.x * pm_size, enemy.y * pm_size))

		draw_text('Current Score: {}'.format(summ),screen, [65,0], 16, White, Font)
		draw_text('High Score:0', screen, [425,0], 16, White, Font)

		pygame.display.flip()
		timer.tick(FPS)
	pygame.display.update()

menu()
