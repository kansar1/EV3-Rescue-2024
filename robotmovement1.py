#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D
import time

right_motor = LargeMotor(OUTPUT_A)
left_motor = LargeMotor(OUTPUT_D)

def straight():
    right_motor.on(75)
    left_motor.on(75)

def turnright():
    right_motor.off()
    left_motor.on(75)

def turnleft():
    right_motor.on(75)
    left_motor.off()

def back():
    right_motor.on(-75)
    left_motor.on(-75)

def off():
    right_motor.off()
    left_motor.off()

straight()
time.sleep(2)
turnright()
time.sleep(2)
turnleft()
time.sleep(2)
back()
time.sleep(2)
