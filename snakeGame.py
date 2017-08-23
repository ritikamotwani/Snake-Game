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
time.sleep(5)
