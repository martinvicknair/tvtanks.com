![TvTanks.com Logo](/assets/images/tvtanktv.JPG)

# My Raspberry Pi Setup

![Raspberry Pi Model B](/assets/images/rpiModelB.jpg)

I'm using an original [Raspberry Pi Model B](https://en.wikipedia.org/wiki/Raspberry_Pi#Model_comparison) with 512mb of RAM.

It's running [Raspberry Pi OS (Legacy)](https://www.raspberrypi.com/software/operating-systems/).

I've also installed the following to allow the Channel Changing functionality:

- [XScreenSaver](https://www.jwz.org/xscreensaver/) - XScreenSaver is the standard screen saver collection shipped on most Linux and Unix systems running the X11 Window System. To install the complete suite, use:

```
sudo apt-get install xscreensaver*
```

My current settings are Random Screen Saver; Blank and Cycle after 1 minute. There are hundreds of [screensavers](https://www.jwz.org/xscreensaver/screenshots/) available: current favorites: BoxFit, CloudLife, Deco, Deluxe, Demon, FuzzyFlakes, Goop, Grav, Kaleidoscope, Moire, Penrose, Phosphor, Pong, PopSquares, Rocks, Squiral, Substrate, WhirlWindWarp, XAnalogTV.

![XScreenSaver-Preferences](/assets/images/xscreensaver-preferences-tvtanks.png)

- Python3 - Did you know that the [name of the Python programming language](https://pythoninstitute.org/about-python) comes from the BBC television comedy sketch called "Monty Python’s Flying Circus"?

```
sudo apt install python3
```

- [pynput](https://pynput.readthedocs.io/en/latest/) - Using Pynput a Python script can simulate a keypress, [move the mouse](https://pynput.readthedocs.io/en/latest/mouse.html) to a specific point on the screen, and monitor the inputs.

```
sudo pip3 install pynput
```

- [GPIO Zero](https://gpiozero.readthedocs.io/en/stable/installing.html) - This library allows a common 2 pole 4 position switch to be [used as a "button"](https://gpiozero.readthedocs.io/en/stable/recipes.html#button) to change the channel on my TvTank. In essence, turning the knob will deactivate the screen saver and set a new background picture.

```
sudo apt install python3-gpiozero
```

<div id="channel_changer.py">
</div>

- Set my channel changer script below at boot. Follow these [instructions](https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/all#method-2-autostart) to use the autostart system, as you will need access to X Windows and the desktop of the Raspberry Pi.

My custom channel changer script is also available on [GitHub](https://github.com/martinvicknair/tvtanks.com/blob/main/channel_changer.py).

```python
#!/usr/bin/env python3

## Changes the 'channel' on my TV Fish tank:
## -Two pole switch connected via GPIO pins of a Raspberry Pi
## -deactivates the screensaver and changes the background picture

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
wp_directory="/home/pi/Desktop/backgrounds/*"

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

## https://tvtanks.com
## https://github.com/martinvicknair
```
