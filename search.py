import pygame
from pygame.locals import *
import math
import random
import datetime

def updateDisplay():
	pygame.display.flip()

def clearScreen():
	screen.fill(bgColor)

def wait(time):
	pygame.time.wait(time)

def draw_cross(eccentricity,angle,color=None):
        if color==None:
                color=fgColor
	
        centerX,centerY = myDisp.returnPhysCoords(eccentricity,angle)
        size = eccentricity / 10.0

	hx1 = centerX - (size / 2.0)
        hy1 = centerY
        hx2 = centerX + (size / 2.0)
        hy2 = centerY

        vx1 = centerX
        vy1 = centerY - (size / 2.0)
        vx2 = centerX
        vy2 = centerY + (size / 2.0)

        rect1 = pygame.Rect(myDisp.phys2pix((hx1, hy1)),myDisp.phys2pix((hx2-hx1,hy2-hy1)))
        rect2 = pygame.Rect(myDisp.phys2pix((vx1, vy1)),myDisp.phys2pix((vx2-vx1,vy2-vy1)))

        pygame.draw.rect(screen,color,rect1)
        pygame.draw.rect(screen,color,rect2)

def draw_l(eccentricity,angle):
	centerX,centerY = myDisp.returnPhysCoords(eccentricity,angle)
	size = eccentricity / 10.0
	lineThickness = size * 0.2
	color = fgColor

	hx1 = centerX - (size / 2.0)
	hy1 = centerY + (size / 2.0)
	hx2 = centerX + (size / 2.0)
	hy2 = centerY + (size / 2.0) - lineThickness

	vx1 = centerX - (size / 2.0)
	vy1 = centerY - (size / 2.0)
	vx2 = centerX - (size / 2.0) + lineThickness
	vy2 = centerY + (size / 2.0)

	rect1 = pygame.Rect(myDisp.phys2pix((hx1, hy1)),myDisp.phys2pix((hx2-hx1,hy2-hy1)))
	rect2 = pygame.Rect(myDisp.phys2pix((vx1, vy1)),myDisp.phys2pix((vx2-vx1,vy2-vy1)))

	pygame.draw.rect(screen,color,rect1)
	pygame.draw.rect(screen,color,rect2)

def draw_t(eccentricity,angle):
        centerX,centerY = myDisp.returnPhysCoords(eccentricity,angle)
        size = eccentricity / 10.0
	color = fgColor
	lineThickness = size * 0.2

	hx1 = centerX - (size / 2.0)
	hy1 = centerY - (size / 2.0) + lineThickness
	hx2 = centerX + (size / 2.0)
	hy2 = centerY - (size / 2.0) 

	vx1 = centerX                - lineThickness / 2.0
	vy1 = centerY - (size / 2.0)
	vx2 = centerX                + lineThickness / 2.0
	vy2 = centerY + (size / 2.0)

        rect1 = pygame.Rect(myDisp.phys2pix((hx1, hy1)),myDisp.phys2pix((hx2-hx1,hy2-hy1)))
        rect2 = pygame.Rect(myDisp.phys2pix((vx1, vy1)),myDisp.phys2pix((vx2-vx1,vy2-vy1)))

	pygame.draw.rect(screen,color,rect1)
	pygame.draw.rect(screen,color,rect2)

def draw_test_markers():
	thisEccentricity = 6.0
	thisAngle = 0.0
	while (thisEccentricity <= 10.0):
		thisAngle = 0.0
		while (thisAngle < 360.0):
			draw_cross(thisEccentricity,thisAngle)
			updateDisplay()
			wait(250)
			thisAngle += 45.0
		thisEccentricity += 2.0

def draw_array(thisEccentricity):
	trialsRunning = True
	totalTrials = 10
	trialCount = 0
	while (trialsRunning):
		totalTrials = 10
		thisTarget = random.randint(0,7)
		thisAngle = 0.0

		clearScreen()
		updateDisplay()
		wait(250)
		i = 0
		while (i < 8):
			if (i == thisTarget):
				draw_t(thisEccentricity,thisAngle)
	#			draw_cross(thisEccentricity,thisAngle,(255,0,0))
			else:
				draw_l(thisEccentricity,thisAngle)
	#			draw_cross(thisEccentricity,thisAngle,(255,0,0))
			thisAngle += 45.0
			i += 1
		updateDisplay()
		wait(2000)	
		trialCount += 1
		if (trialCount > totalTrials):
			trialsRunning = False

class PhysicalDisplay:

	def __init__(self,thisDiagonal,thisAspect,thisResolution,thisDistance=None):
		self.diagonal = thisDiagonal
		self.aspect = thisAspect
		self.resolution = thisResolution
		if thisDistance==None:
			# default distance is 57cm
			self.distance = 57
		else:
			self.distance = thisDistance
		diagAspect = math.hypot(self.aspect[0],self.aspect[1])
		self.width = self.aspect[0] * (self.diagonal / diagAspect)
		self.height = self.aspect[1] * (self.diagonal / diagAspect)
		self.origin = (self.width/2.0,self.height/2.0)
	def returnPhysCoords(self,eccentricity,angle):
		offCenter = self.distance * math.tan(math.radians(eccentricity))
		physCoordsX = self.origin[0] + (offCenter * math.cos(math.radians(angle)))
		physCoordsY = self.origin[1] + (offCenter * math.sin(math.radians(angle)))
		return (physCoordsX,physCoordsY)
	def phys2pix(self,physCoords):	
		pixCoordsX = physCoords[0] * (self.resolution[0] / self.width)
		pixCoordsY = physCoords[1] * (self.resolution[1] / self.height)
		return (pixCoordsX,pixCoordsY)
	def returnPixCoords(self,eccentricity,angle):
		return self.phys2pix(self.returnPhysCoords(eccentricity,angle))

pygame.init()
modes = pygame.display.list_modes();
screen = pygame.display.set_mode(modes[0], (FULLSCREEN | DOUBLEBUF | HWSURFACE))
pygame.mouse.set_visible(0)

bgColor = (0,0,0)
fgColor = (255,255,255)

MacBookDiag = 13.3      
MacBookAspect = (16,10) 

CinemaDisplay23Diag = 23
CinemaDisplay23Aspect = (16,10)

#myDisp = PhysicalDisplay(MacBookDiag * 2.54,MacBookAspect,modes[0])
myDisp = PhysicalDisplay(CinemaDisplay23Diag * 2.54,CinemaDisplay23Aspect,modes[0])

screenSizeX = modes[0][0]
screenSizeY = modes[0][1]

screenCenterX = screenSizeX / 2.0
screenCenterY = screenSizeY / 2.0


random.seed(datetime.datetime.microsecond)
