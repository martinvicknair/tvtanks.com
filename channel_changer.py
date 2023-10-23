#!/usr/bin/env python3

# Changes the 'channel' on my TV Fish tank:
# -Two pole switch connected via GPIO pins of a Raspberry Pi
# -deactivates the screensaver and changes the background picture

# Import modules
import glob
import random
import os
from gpiozero import Button
from pynput.mouse import Controller
from signal import pause
from subprocess import call

# Initialize mouse controller
mouse = Controller()
# Initialize button on GPIO pin 2
button = Button(2)

# Store directory of wallpapers in variable
wp_directory = "/home/pi/Desktop/backgrounds/*"

# Sets initial mouse position away from center of screen
mouse.position = (0, 50)

# Define action to be taken when button is pressed or released


def action():
    # Deactivate screensaver and move mouse away from center of screen
    os.system("xscreensaver-command -deactivate")
    mouse.position = (0, 50)
# Select a random wallpaper from the directory
    random_file = random.choice(glob.glob(wp_directory))
# Set the wallpaper using pcmanfm
    call(["pcmanfm", "--set-wallpaper=" + random_file])


# Set action to be taken when button is pressed or released
button.when_pressed = action
button.when_released = action

# Pause program execution until button is pressed or released
pause()

# https://pynput.readthedocs.io/en/latest/index.html
# https://gpiozero.readthedocs.io/en/stable/
# https://gpiozero.readthedocs.io/en/stable/recipes.html#button
# https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/all#method-2-autostart

# https://tvtanks.com
# https://github.com/martinvicknair
