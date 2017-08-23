#Snake Game!

import pygame
import sys
import random
import time

check_errors = pygame.init()
if check_errors[1] > 0:
	print("Errors")
	sys.exit(-1)
else:
	print("Successful")
#Play Surface
playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake Game')


#Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)



# FPS controller(Frame Per Second)
fpsController = pygame.time.Clock()

#Important Variables
snakePos = [100,50]
snakeBody = [[100,50][90,50][80,50]]
