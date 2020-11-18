import pygame, sys
import numpy as np
import random
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

def game():
#Game loop 
	global a, b, da, db, z, t, dz, dx, dy, dt, x, y, pm_open_left, pm_open, pm_open_down, pm_open_left, pm_open_up, block, logo, background, ghost, ghost2, look_open_up, look_open_down, look_open_left
	
	pygame.mixer.init()
	pygame.mixer.music.load('wap.mp3')
	pygame.mixer.music.play(-1, 0.0)
	
	while True:
	 	###############################Ghost 1 boundaries############################################
		save_z, save_t = z,t

		z = z + dz
		rect3 = pygame.Rect(z,t,pm_size,pm_size)
		collide = False
		for i in range(len(pm_maze)):
			for j in range(len(pm_maze[i])):
				if pm_maze[i][j] == 0 or pm_maze[i][j] == 6 or pm_maze[i][j] == 7 or pm_maze[i][j] == 8:
					rect2 = pygame.Rect(j*pm_size,i*pm_size,pm_size,pm_size)
					if rect3.colliderect(rect2):
						collide = True
				elif pm_maze[i][j] == 1 or pm_maze[i][j] == 4:
					rect2 = pygame.Rect(j*pm_size,i*pm_size,pm_size,pm_size)
					if pm_maze[i][j] == 5:
						if rect3.colliderect(rect2):
							collide = True
							pm_maze[i][j] == 8


		if collide:
			z = save_z
			dz = 0

		t = t + dt
		rect3 = pygame.Rect(z, t, pm_size, pm_size)
		collide = False
		for i in range(len(pm_maze)):
			for j in range(len(pm_maze[i])):
				if pm_maze[i][j] == 0 or pm_maze[i][j] == 6 or pm_maze[i][j] == 7:
					rect2 = pygame.Rect(j*pm_size, i*pm_size, pm_size, pm_size)
					if rect3.colliderect(rect2):
						collide = True

		if collide:
			t = save_t
			dt = 0

		for number in range(100000):
			number = random.randint(-2, 1)
			if number == -2:
				dt, dz = 20, 0
			elif number == -1:
				dt, dz = -20, 0
			elif number == 0:
				dt, dz = 0, 20
			elif number == 1:
				dt, dz = 0, -20

	####################################Ghost2 boundaries#######################################
		save_a, save_b = a, b

		a = a + da
		rect3 = pygame.Rect(a, b, pm_size, pm_size)
		collide = False
		rect3 = pygame.Rect(a, b, pm_size, pm_size)
		collide = False
		for i in range(len(pm_maze)):
			for j in range(len(pm_maze[i])):
				if pm_maze[i][j] == 0 or pm_maze[i][j] == 6 or pm_maze[i][j] == 7:
					rect2 = pygame.Rect(j*pm_size,i*pm_size,pm_size,pm_size)
					if rect3.colliderect(rect2):
						collide = True


		if collide:
			a = save_a
			da = 0

		b = b + db
		rect3 = pygame.Rect(a, b, pm_size, pm_size)
		collide = False
		for i in range(len(pm_maze)):
			for j in range(len(pm_maze[i])):
				if pm_maze[i][j] == 0 or pm_maze[i][j] == 6 or pm_maze[i][j] == 7:
					rect2 = pygame.Rect(j*pm_size, i*pm_size, pm_size, pm_size)
					if rect3.colliderect(rect2):
						collide = True

		if collide:
			b = save_b
			db = 0

		###############################Pacman boundaries#########################################	
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
					dx = 0
					dy = -20
					da = 0
					db = 20
					look_open_up = True
					look_open_left = False
					look_open_down = False
				elif event.key == pygame.K_DOWN:
					dx = 0
					dy = 20
					da = 0
					db = -20
					look_open_down = True
					look_open_left = False
					look_open_up = False
				elif event.key == pygame.K_LEFT:
					dx = -20
					dy = 0
					da = 20
					db = 0
					look_open_left = True
					look_open_up = False
					look_open_down = False
				elif event.key == pygame.K_RIGHT:
					dx = 20
					dy = 0
					da = -20
					db = 0
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
		
		screen.blit(ghost1, (z, t))
		screen.blit(ghost2, (a, b))
		draw_text('Current Score: {}'.format(summ),screen, [65,0], 16, White, Font)
		draw_text('High Score:0', screen, [425,0], 16, White, Font)

		pygame.display.flip()
		timer.tick(FPS)
	#pygame.display.update()

menu()
scores_maximum.append(scores_max)
print(scores_maximum)
