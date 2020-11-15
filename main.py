import pygame
from char import  *  # * - same folder
from maze_pacman import  *
vec = pygame.math.Vector2
pygame.init()

screen = pygame.display.set_mode((Width,Height))
pm_size = 20
# caption and icon 
pygame.display.set_caption("PacMan")
pygame.display.set_icon(logo)

pygame.mixer.init()
pygame.mixer.music.load('wap.mp3')
pygame.mixer.music.play(-1, 0.0)

# Это функция которая передает текст, который отображается в на экране.
def draw_text(words, screen, pos, size, color, font_name, centered=False):
	font = pygame.font.SysFont(font_name, size)
	text = font.render(words, False, color)
	screen.blit(text,pos)

coin = []
#Game loop 
while True:
	save_x, save_y = x, y 

	y = y+dy
	rect1 = pygame.Rect(x,y,pm_size,pm_size)
	collide = False
	for i in range(len(pm_maze)):
		for j in range(len(pm_maze[i])):
			if pm_maze[i][j] == 0 or pm_maze[i][j] == 5:
				rect2 = pygame.Rect(j*pm_size,i*pm_size,pm_size,pm_size)
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


	summ = -10
	for i in coin:
		summ += i

	screen.fill(Black)
	
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				dx = 0
				dy = -20
				look_open_up = True
				look_open_left = False
				look_open_down = False
			elif event.key == pygame.K_DOWN:
				dx = 0
				dy = 20
				look_open_down = True
				look_open_left = False
				look_open_up = False
			elif event.key == pygame.K_LEFT:
				dx = -20
				dy = 0
				look_open_left = True
				look_open_up = False
				look_open_down = False
			elif event.key == pygame.K_RIGHT:
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
	
	draw_text('Current Score: {}'.format(summ),screen, [65,0], 16, White, Font)
	draw_text('High Score:0', screen, [425,0], 16, White, Font)

	pygame.display.flip()
	timer.tick(FPS)
	#pygame.display.update()