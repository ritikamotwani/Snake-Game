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
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

#Game Over function
def gameOver():
	myFont = pygame.font.SysFont('monaco', 72)
	GOsurf = myFont.render('Game Over!', True, red)
	GOrect = GOsurf.get_rect()
	GOrect.midtop = (360, 15)
	playSurface.blit(GOsurf, GOrect)
	pygame.display.flip()
	time.sleep(4)
	pygame.quit()
	sys.exit()


#Main Logic of the Game
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT:
				changeto = 'LEFT'
			if event.key == pygame.K_UP:
				changeto = 'UP'
			if event.key == pygame.K_DOWN:
				changeto = 'DOWN'
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
			
	# validation of direction

	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'
	# Update snake position [x,y]
	if direction == 'RIGHT':
		snakePos[0] += 10
	if direction == 'LEFT':
		snakePos[0] -= 10
	if direction == 'UP':
		snakePos[1] -= 10
	if direction == 'DOWN':
		snakePos[1] += 10

	# Snake body mechanism
	snakeBody.insert(0, list(snakePos))
	if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
		foodSpawn = False
	else:
		snakeBody.pop()
	if foodSpawn == False:
		foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
 	foodSpawn = True

	# Background
	playSurface.fill(white)
	
	for pos in snakeBody:
		pygame.draw.rect(playSurface, green, pygame.Rect(pos[0],pos[1],10,10))
	pygame.display.flip()
	fpsController.tick(25)	
