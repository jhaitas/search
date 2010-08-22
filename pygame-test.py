#! /usr/bin/env python

import sys,os
import search


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
search.wait(20000)

search.clearScreen()
search.updateDisplay()

search.draw_l(10.0,0.0)
search.draw_t(10.0,180.0)
search.updateDisplay()
search.wait(20000)

search.clearScreen()
search.updateDisplay()

search.draw_l(8.0,90.0)
search.draw_t(8.0,270.0)
search.updateDisplay()
search.wait(20000)

