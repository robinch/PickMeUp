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
	pygame.key.set_repeat(3,1)
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
	#cat2Img = pygame.image.load('cat.png')
	catX = 10
	catY = 10
	#cat2X = 200
	#cat2Y = 200
	direction = 'right'
	
	# set up sound
	pygame.mixer.music.load('mjau.wav')
	
	pygame.mixer.music.play(-1, 0.0)
	while  True:	
		DISPLAYSURF.blit(bg, (0, 0))
		DISPLAYSURF.blit(catImg, (catX, catY))
		#DISPLAYSURF.blit(cat2Img, (cat2X, cat2Y))
		#event handler
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				# Figure out if it was an arrow key. If so
            	# adjust speed.
				if event.key == pygame.K_LEFT:
					catX -= 5
				if event.key == pygame.K_RIGHT:
					catX += 5
				if event.key == pygame.K_UP:
					catY -= 3
				if event.key == pygame.K_DOWN:
					catY += 3
				#uncoment if you want to enable 2 player
				#if event.key == pygame.K_a:
				#	cat2X -= 5
				#if event.key == pygame.K_d:
				#	cat2X += 5
				#if event.key == pygame.K_w:
				#	cat2Y -= 3
				#if event.key == pygame.K_s:
				#	cat2Y += 3
	
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
gameLoop()