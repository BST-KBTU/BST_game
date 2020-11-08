import pygame
from char import  *  # * - same folder

pygame.init()

screen = pygame.display.set_mode((Width,Height))

# caption and icon 
pygame.display.set_caption("PacMan")
img = pygame.image.load("pmlogo.jpg")
pygame.display.set_icon(img)

# background
background = pygame.image.load('maze.png')
background = pygame.transform.scale(background,(maze_width,maze_height))

timer = pygame.time.Clock()

def draw_boundaries(color):
	for x in range(29):
		pygame.draw.line(background, color, (x*20, 0),(x*20, Height+25))
	for y in range(32):
		pygame.draw.line(background, color, (0, y*20),(Width+25,y*20))

def draw_text(words, screen, pos, size, color, font_name, centered=False):
	font = pygame.font.SysFont(font_name, size)
	text = font.render(words, False, color)
	screen.blit(text,pos)

while True:

	for event in pygame.event.get(): 
		if event.type == pygame.QUIT:
			pygame.quit()

	screen.fill(Black)	
	screen.blit(background, (25,25))

	draw_boundaries(Grey)
	draw_text('Current Score:0',screen, [65,0], 16, White, Font)
	draw_text('High Score:0', screen, [425,0], 16, White, Font)
	pygame.display.flip()
	timer.tick(FPS)
	pygame.display.update()
	