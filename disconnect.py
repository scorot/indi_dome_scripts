#!/usr/bin/python
#
# Connect script for INDI Dome Scripting Gateway
#
# Arguments: none
# Exit code: 0 for success, 1 for failure
#

import sys

import RPi.GPIO as GPIO
import time

# CH1 -> pin 35
# CH2 -> pin 37
# CH3 -> pin 38
# CH4 -> pin 40
pin = 35

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
GPIO.cleanup()


sys.exit(0)
