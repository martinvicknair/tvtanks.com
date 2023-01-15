#!/usr/bin/env python3

## Changes the 'channel' on my TV Fish tank:
## -Two pole switch connected via GPIO pins of a Raspberry Pi
##  deactivates the screensaver and changes the background picture

import os
from pynput.mouse import Button, Controller
from gpiozero import Button
from signal import pause

mouse = Controller()
button = Button(2)

# Sets initial mouse position away from center of screen
mouse.position = (0, 50)


def action():
    os.system("/home/pi/Desktop/random_bg")
    os.system("xscreensaver-command -deactivate")
    mouse.position = (0, 50)


button.when_pressed = action
button.when_released = action

pause()

# https://pynput.readthedocs.io/en/latest/index.html
# https://gpiozero.readthedocs.io/en/stable/
# https://gpiozero.readthedocs.io/en/stable/recipes.html#button
# https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/all#method-2-autostart
#
## https://tvtanks.com
## https://github.com/martinvicknair
