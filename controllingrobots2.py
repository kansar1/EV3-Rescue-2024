#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D
import time

right_motor = LargeMotor(OUTPUT_A)
left_motor = LargeMotor(OUTPUT_D)

# Right motor at 100%.
right_motor.on(100)

# Left motor at 75%.
left_motor.on(75)

# Wait 10 seconds before proceeding to end the program
time.sleep(10)