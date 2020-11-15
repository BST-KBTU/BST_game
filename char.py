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
Pink = (255, 192, 203)
#font
Font = 'arial black'
Text_size = 20

pm_size = 20

#load images

pm_close = pygame.image.load("pacman_close.png")
pm_close_down = pygame.image.load("pacman_close_down.png")
pm_close_left = pygame.image.load("pacman_close_left.png")
pm_close_up = pygame.image.load("pacman_close_up.png")
pm_open = pygame.image.load("pacman_open.png")
pm_open_down = pygame.image.load("pacman_open_down.png")
pm_open_left = pygame.image.load("pacman_open_left.png")
pm_open_up = pygame.image.load("pacman_open_up.png")
block = pygame.image.load("Purple_Block.png")
logo = pygame.image.load("pmlogo.jpg")
background = pygame.image.load('maze.png')
background = pygame.transform.scale(background,(maze_width,maze_height))
pm_close_up = pygame.transform.scale(pm_close_up, (pm_size, pm_size))
pm_close = pygame.transform.scale(pm_close, (pm_size, pm_size))
pm_close_down = pygame.transform.scale(pm_close_down, (pm_size, pm_size))
pm_close_left = pygame.transform.scale(pm_close_left, (pm_size, pm_size))
pm_open = pygame.transform.scale(pm_open, (pm_size, pm_size))
pm_open_up = pygame.transform.scale(pm_open_up, (pm_size, pm_size))
pm_open_down = pygame.transform.scale(pm_open_down, (pm_size, pm_size))
pm_open_left = pygame.transform.scale(pm_open_left, (pm_size, pm_size))
block = pygame.transform.scale(block,(pm_size,pm_size))
timer = pygame.time.Clock()

look_open_up = False
look_open_down = False
look_open_left = False
x = 40
y = 100
dx = 0 # horizontal speed
dy = 0 # vertical speed 