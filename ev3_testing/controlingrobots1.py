#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D

right_motor = LargeMotor(OUTPUT_A)
left_motor = LargeMotor(OUTPUT_D)

# Right motor at 80% for 3 seconds.
right_motor.on_for_seconds(80, 3)

# Left motor at 30% for 5 full rotations.
left_motor.on_for_rotations(30, 5)

print("Done!")