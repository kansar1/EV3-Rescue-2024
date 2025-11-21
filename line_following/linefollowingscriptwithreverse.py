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

timeSinceBack = 0

def straight():
    right_motor.on(35)
    left_motor.on(35)

def turnright():
    right_motor.on(-20)
    left_motor.on(40)

def turnleft():
    right_motor.on(40)
    left_motor.on(-20)
        

def back():
    right_motor.on(-80)
    left_motor.on(-80)

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

    if r1 >= 50 and g1 >= 50 and b1 >= 50 and r2 >= 50 and g2 >= 50 and b2 >= 50:
        straight()
        time.sleep(0.02)

    if r1 <= 50 and g1 <=50 and b1 <= 50:
        if timeSinceBack > 0.5:
            back()
            time.sleep(0.02)
            timeSinceBack = 0
            off()
        turnright() 

    if r2 <= 50 and g2 <=50 and b2 <= 50:
        if timeSinceBack > 0.5:
            back()
            time.sleep(0.02)
            timeSinceBack = 0
            off()
        turnleft()

    timeSinceBack += 0.02