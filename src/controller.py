#!/usr/bin/env python

#import evdev
import rospy
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event2')

#button code variables (change to suit your device)

print(gamepad)

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
		print("X Axis: " + str(event.value))
	elif event.code == 1:
		print("Y Axis: " + str(event.value))
	elif event.code == 2:
		print("Z Axis: " + str(event.value))
	else:
		print("UNRECOGNIZED MOVEMENT")




