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

ghost1 = pygame.image.load('Pacman_red 1.png')
ghost2 = pygame.image.load('Pacman_pink.png')

pm_open = pygame.transform.scale(pm_open, (pm_size, pm_size))
pm_open_up = pygame.transform.scale(pm_open_up, (pm_size, pm_size))
pm_open_down = pygame.transform.scale(pm_open_down, (pm_size, pm_size))
pm_open_left = pygame.transform.scale(pm_open_left, (pm_size, pm_size))
block = pygame.transform.scale(block,(pm_size, pm_size))
ghost1 = pygame.transform.scale(ghost1,(pm_size, pm_size))
ghost2 = pygame.transform.scale(ghost2, (pm_size, pm_size))

look_open_up = False
look_open_down = False
look_open_left = False

x = 40
y = 100
dx = 0 # horizontal speed
dy = 0 # vertical speed 

z = 300 #coordinate of the ghost 
t = 300 #coordinate of the ghost
dz = 0
dt = 0

a = 280
b = 280
da = 0
db = 0
