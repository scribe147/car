import RPi.GPIO as GPIO
import curses
import time
from curses import wrapper

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

stdscr = curses.initscr()
stdscr.clear()

while True:
    ch = stdscr.getkey()
# Quit 
    if ch == 'q':
       curses.endwin()
       GPIO.output(4, False)
       GPIO.output(17, False)
       GPIO.output(27, False)
       GPIO.output(22, False)
       break

# Forward
    if ch == 'w':
       GPIO.output(17, False)
       GPIO.output(4,  True)
       GPIO.output(22, False)
       GPIO.output(27, True)

# Backward
    if ch == 'x':
       GPIO.output(17, True)
       GPIO.output(4, False)
       GPIO.output(22, True)
       GPIO.output(27, False)

# Turn Right
    if ch == 'd':
       GPIO.output(17, False)
       GPIO.output(4, True)
       GPIO.output(22, False)
       GPIO.output(27, False)

# Turn Left
    if ch == 'a':
       GPIO.output(17, False)
       GPIO.output(4, False)
       GPIO.output(22, False)
       GPIO.output(27, True)
RPIO.cleanup()
