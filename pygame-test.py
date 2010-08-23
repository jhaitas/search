#! /usr/bin/env python

import sys,os
import search
import random
import datetime

random.seed(datetime.datetime.microsecond)

thisEccentricity = 6.0
thisAngle = 0.0
while (thisEccentricity <= 10.0):
	thisAngle = 0.0
	while (thisAngle < 360.0):
		search.draw_cross(thisEccentricity,thisAngle)
		search.updateDisplay()
		search.wait(250)
		thisAngle += 45.0
	thisEccentricity += 2.0
#search.wait(5000)

trialsRunning = True
trialCount = 0
while (trialsRunning):
	totalTrials = 10
	thisTarget = random.randint(0,7)
	thisEccentricity = 8.0
	thisAngle = 0.0

	search.clearScreen()
	search.updateDisplay()
	search.wait(250)
	i = 0
	while (i < 8):
		if (i == thisTarget):
			search.draw_t(thisEccentricity,thisAngle)
#			search.draw_cross(thisEccentricity,thisAngle,(255,0,0))
		else:
			search.draw_l(thisEccentricity,thisAngle)
#			search.draw_cross(thisEccentricity,thisAngle,(255,0,0))
		thisAngle += 45.0
		i += 1
	search.updateDisplay()
	search.wait(2000)	
	trialCount += 1
	if (trialCount > totalTrials):
		trialsRunning = False

	

