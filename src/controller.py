#!/usr/bin/env python

import rospy
import numpy
import math
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event2')

#button code variables (change to suit your device)

print(gamepad)

xaxis = 128
yaxis = 128

def button_status(name, value):
	if value == 1:
		print(name + " Pressed")
	elif value == 0:
		print(name + " Depressed")
	else:
		print(name + " Unknown Value")

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
	if event.code == 298:
		button_status("Button 11", event.value)
	elif event.code == 297:
		button_status("Button 10", event.value)
	elif event.code == 296:
                button_status("Button 9", event.value)
	elif event.code == 295:
                button_status("Button 8", event.value)
	elif event.code == 294:
                button_status("Button 7", event.value)
	elif event.code == 293:
                button_status("Button 6", event.value)
	elif event.code == 292:
                button_status("Button 5", event.value)
	elif event.code == 291:
                button_status("Button 4", event.value)
	elif event.code == 290:
                button_status("Button 3", event.value)
	elif event.code == 289:
                button_status("Button 2", event.value) 
	elif event.code == 288:
                button_status("Trigger", event.value)
	else:
		print("UNREGONIZED BUTTON") 
    if event.type == ecodes.EV_ABS:
	if event.code == 0:
		xaxis = event.value
	elif event.code == 1:
		yaxis = event.value
	elif event.code == 2:
		print("Z Axis: " + str(event.value))
	else:
		print("UNRECOGNIZED MOVEMENT")

    xfrac = 0.0
    if xaxis > 135:
	xfrac = (float(xaxis)-135)/120
    elif xaxis < 121:
	xfrac = -1.0+(float(xaxis)/(121))

    yfrac = 0.0
    if yaxis > 135:
        yfrac = ((float(yaxis)-135)/(-120))
    elif yaxis < 121:
        yfrac = 1.0-(float(yaxis)/(121))

    print(xfrac, yfrac)
    angle = math.degrees(numpy.arctan2(yfrac,xfrac))
    angle = angle - 90
    if angle < 0:
	angle = angle + 360
    mag = math.sqrt((yfrac**2) + (xfrac**2))
    if mag > 1.0:
	mag = 1.0
    print("angle: " + str(angle))
    print("mag: " + str(mag))
