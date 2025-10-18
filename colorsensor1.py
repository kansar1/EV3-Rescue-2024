#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import ColorSensor
import time
from ev3sim.code_helpers import wait_for_tick

# Instantiate the colour sensor
cs = ColorSensor(INPUT_2)

# Infinite loop to run forever
while True:
    wait_for_tick() # All loops in the simulator must start with wait_for_tick

    # cs.rgb returns a list of 3 values. These can be unpacked like so:
    r, g, b = cs.rgb

    # Print these values and then pause for 0.5 seconds
    print("Raw values (Scaled to 255): {}, {}, {}.".format(r, g, b))
    time.sleep(0.5)