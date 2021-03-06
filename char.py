from pygame.math import Vector2 as vec
import pygame
Width, Height = 600, 670
maze_width, maze_height = 560, 620  
FPS=3

#colours
Black = (0,0,0)
Grey = (107, 107, 107)
White = (255,255,255)
Yellow = (255, 215, 0)
Pink = (255,192,203)
Blue = (0, 0, 80)
Red = (255, 0, 0)
#font
Font = 'arial black'
Text_size = 20

pm_size = 20

#load images


pm_open = pygame.image.load("pacman_open.png")
pm_open_down = pygame.image.load("pacman_open_down.png")
pm_open_left = pygame.image.load("pacman_open_left.png")
pm_open_up = pygame.image.load("pacman_open_up.png")
block = pygame.image.load("Purple_Block.png")
logo = pygame.image.load("pmlogo.jpg")
logo1 = pygame.image.load("logo1.png")
f1 = pygame.image.load("f1.png")
cute = pygame.image.load("cute.jpg")

ghost1 = pygame.image.load('Pacman_red 1.png')
ghost2 = pygame.image.load('Pacman_pink.png')
ghost3 = pygame.image.load('Pacman_orange.png')
ghost4 = pygame.image.load('Pacman_mint.png')

hat = pygame.image.load("hat.png")

pm_open = pygame.transform.scale(pm_open, (pm_size, pm_size))
pm_open_up = pygame.transform.scale(pm_open_up, (pm_size, pm_size))
pm_open_down = pygame.transform.scale(pm_open_down, (pm_size, pm_size))
pm_open_left = pygame.transform.scale(pm_open_left, (pm_size, pm_size))
block = pygame.transform.scale(block,(pm_size, pm_size))
ghost1 = pygame.transform.scale(ghost1,(pm_size, pm_size))
ghost2 = pygame.transform.scale(ghost2, (pm_size, pm_size))
ghost3 = pygame.transform.scale(ghost3, (pm_size, pm_size))
ghost4 = pygame.transform.scale(ghost4, (pm_size, pm_size))
ghost5 = pygame.transform.scale(ghost1, (100, 100))
cute = pygame.transform.scale(cute, (600 ,670))

hat = pygame.transform.scale(hat, (80, 90))

bghost1 = pygame.transform.scale(ghost1, (60, 60))
bghost2 = pygame.transform.scale(ghost2, (60, 60))
bghost3 = pygame.transform.scale(ghost3, (60, 60))
bghost4 = pygame.transform.scale(ghost4, (60, 60))
bpacman = pygame.transform.scale(pm_open, (60, 60))

f1 = pygame.transform.scale(f1, (300, 300))

look_open_up = False
look_open_down = False
look_open_left = False

x = 40
y = 100
dx = 0 # horizontal speed
dy = 0 # vertical speed 
