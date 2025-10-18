#!/usr/bin/env python3

from ev3dev2.sensor import INPUT_2, INPUT_1, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3sim.code_helpers import wait_for_tick
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D
import time

# Instantiate the colour sensor
csright = ColorSensor(INPUT_2)
csleft = ColorSensor(INPUT_3)

# Define motors and commands
right_motor = LargeMotor(OUTPUT_A)
left_motor = LargeMotor(OUTPUT_D)

def straight():
    right_motor.on(30)
    left_motor.on(30)

def turnright():
    right_motor.off()
    left_motor.on(60)

def turnleft():
    right_motor.on(60)
    left_motor.off()

def rightgreen():
    straight()
    time.sleep(0.1)
    off()
    time.sleep(0.1)
    right_motor.off()
    left_motor.on(90)

def leftgreen():
    straight()
    time.sleep(0.1)
    off()
    time.sleep(0.1)
    right_motor.on(90)
    left_motor.off()
    
def back():
    right_motor.on(-40)
    left_motor.on(-40)

def off():
    right_motor.off()
    left_motor.off()
    
# Infinite loop to run forever
while True:
    wait_for_tick() # All loops in the simulator must start with wait_for_tick

    # cs.rgb returns a list of 3 values. These can be unpacked like so:
    r1, g1, b1 = csright.rgb
    r2, g2, b2 = csleft.rgb

    print("Raw values (Scaled to 255): {}, {}, {}.".format(r1, g1, b1))

    if r1 <= 50 and g1 >= 100 and b1 <= 50 and ((r2 >= 50 and g2 >= 50 and b2 >= 50) or (r2 <= 50 and g2 <= 50 and b2 <= 50)):
        r1, g1, b1 = csright.rgb
        r2, g2, b2 = csleft.rgb
        rightgreen()
        
    elif r2 <= 50 and g2 >= 100 and b2 <= 50 and ((r1 >= 50 and g1 >= 50 and b1 >= 50) or (r1 <= 50 and g1 <= 50 and b1 <= 50)):
        r1, g1, b1 = csright.rgb
        r2, g2, b2 = csleft.rgb
        leftgreen()

    elif r1 <= 90 and g1 <= 90 and b1 <= 90:
        turnright() 

    elif r2 <= 90 and g2 <= 90 and b2 <= 90:
        turnleft() 

    elif r1 >= 50 and g1 >= 50 and b1 >= 50 and r2 >= 50 and g2 >= 50 and b2 >= 50:
        straight()