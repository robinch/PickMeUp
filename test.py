import pygame, sys
from pygame.locals import *
import time
from threading import Thread

pygame.init()

background = (pygame.image.load('bg.jpg'), pygame.image.load('eiffel_tower.jpg'), pygame.image.load('cloudy_sky.jpg'))
bg = background[0]

# run the game loop
def gameLoop():
	global bg
	global changeLoop
	changeLoop.start()
	FPS = 30 # frames per second setting
	fpsClock = pygame.time.Clock()
	
	# set up the window
	DISPLAYSURF = pygame.display.set_mode((800,600), 0, 32)
	pygame.display.set_caption('PickMeUp')
	
	BLACK	= 	(0 , 0, 0)
	WHITE	=	(255,255,255)
	RED		= 	(255,0,0)
	GREEN 	= 	(0,255,0)
	BLUE 	= 	(0,0,255)
	YELLOW	=	(255,255,0)
	
	DISPLAYSURF.fill(WHITE)
	
	# set up images
	
	# set up catimage
	catImg = pygame.image.load('cat.png')
	catX = 10
	catY = 10
	direction = 'right'
	
	# set up sound
	pygame.mixer.music.load('mjau.wav')
	
	pygame.mixer.music.play(-1, 0.0)
	while  True:	
		DISPLAYSURF.blit(bg, (0, 0))
		if direction == 'right':
			catX += 5
			if catX == 280:
				direction = 'down'
		elif direction == 'down':
			catY += 5
			if catY == 220:
				direction = 'left'
		elif direction == 'left':
			catX -= 5
			if catX == 10:
				direction = 'up'
		elif direction == 'up':
			catY -= 5
			if catY == 10:
				direction = 'right'

		DISPLAYSURF.blit(bg, (0, 0))
		DISPLAYSURF.blit(catImg, (catX, catY))

		#event handler
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			pygame.display.update()
	
		pygame.display.update()
		fpsClock.tick(FPS)
	return
 
def changeBG():
	global bg
	while True:
		time.sleep(3)
		if bg == background[0]:
			bg = background[1]
		elif bg == background[1]:
			bg = background[2]
		elif bg == background[2]:
			bg = background[0]
	return

changeLoop = Thread(target=changeBG)
<<<<<<< HEAD
gameLoop()
=======

#This row is to check if it updates
>>>>>>> b99d15a577a2bd21199da7ab3d34ade38328dd37
