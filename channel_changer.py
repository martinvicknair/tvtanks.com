#!/usr/bin/env python3

## Changes the 'channel' on my TV Fish tank:
## -Two pole switch connected via GPIO pins of a Raspberry Pi
## -deactivates the screensaver and changes the background picture

import os
from pynput.mouse import Button, Controller
from gpiozero import Button
from signal import pause
import glob
import random
from subprocess import call

mouse = Controller()  # Initialize mouse controller 
button = Button(2)    # Initialize button on GPIO pin 2 

# Store directory of wallpapers in variable 
wp_directory="/home/pi/Desktop/backgrounds/*"

# Sets initial mouse position away from center of screen 
mouse.position = (0, 50)

# Define action to be taken when button is pressed or released 
def action():  

# Select a random wallpaper from the directory 
    random_file = random.choice(glob.glob(wp_directory))

# Set the wallpaper using pcmanfm  
    call(["pcmanfm", "--set-wallpaper=" + random_file])  

# Deactivate screensaver and move mouse away from center of screen 
    os.system("xscreensaver-command -deactivate")  
    mouse.position = (0, 50)  

# Set action to be taken when button is pressed or released 
button.when_pressed = action  
button.when_released = action  

# Pause program execution until button is pressed or released 
pause()  

# https://pynput.readthedocs.io/en/latest/index.html
# https://gpiozero.readthedocs.io/en/stable/
# https://gpiozero.readthedocs.io/en/stable/recipes.html#button
# https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/all#method-2-autostart

## https://tvtanks.com
## https://github.com/martinvicknair
