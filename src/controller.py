#!/usr/bin/env python

import rospy
import numpy
import math
import evdev
#from evdev import InputDevice, categorize, ecodes
from std_msgs.msg import Float64

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
	if device.name == 'Logitech Logitech Attack 3':
		gamepad = evdev.InputDevice(device.path)

#button code variables (change to suit your device)

print(gamepad)

xaxis = 128
yaxis = 128
zaxis = 0
raxis = 0
depth = 0.0

def button_status(name, value):
	if value == 1:
		print(name + " Pressed")
	elif value == 0:
		print(name + " Depressed")
	else:
		print(name + " Unknown Value")

trans_vec_pub = rospy.Publisher('translational_vector', Float64, queue_size=1)
trans_mag_pub = rospy.Publisher('translational_magnitude', Float64, queue_size=1)
rot_vec_pub = rospy.Publisher('rotational_vector', Float64, queue_size=1)
rot_mag_pub = rospy.Publisher('rotational_magnitude', Float64, queue_size=1)
depth_effort_pub = rospy.Publisher('depth_effort', Float64, queue_size=10)
depth_setpoint_pub = rospy.Publisher('depth_setpoint', Float64, queue_size=10)
rospy.init_node('Joystick_controller', anonymous=True)


#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if rospy.is_shutdown():
	break
    if event.type == evdev.ecodes.EV_KEY:
	if event.code == 298:
		button_status("Button 11", event.value)
	elif event.code == 297:
		button_status("Button 10", event.value)
	elif event.code == 296:
		raxis = raxis + 2
	elif event.code == 295:
		raxis = raxis - 2
	elif event.code == 294:
                button_status("Button 7", event.value)
	elif event.code == 293:
                button_status("Button 6", event.value)
	elif event.code == 292:
                button_status("Button 5", event.value)
	elif event.code == 291:
                button_status("Button 4", event.value)
	elif event.code == 290:
		depth = depth - .1
	elif event.code == 289:
		depth = depth + .1
	elif event.code == 288:
                button_status("Trigger", event.value)
	else:
		print("UNREGONIZED BUTTON") 
    if event.type == evdev.ecodes.EV_ABS:
	if event.code == 0:
		xaxis = event.value
	elif event.code == 1:
		yaxis = event.value
	elif event.code == 2:
		zaxis = event.value
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

    angle = math.degrees(numpy.arctan2(yfrac,xfrac))
    angle = angle - 90
    if angle < 0:
	angle = angle + 360
    mag = math.sqrt((yfrac**2) + (xfrac**2))
    if mag > 1.0:
	mag = 1.0

    zaxisfloat = float(zaxis)/256

    trans_vec_pub.publish(float(angle))
    trans_mag_pub.publish(float(mag))
    rot_vec_pub.publish(numpy.sign(raxis))
    rot_mag_pub.publish(numpy.abs(raxis))
    #depth_effort_pub.publish(zaxisfloat)
    depth_setpoint_pub.publish(depth)
