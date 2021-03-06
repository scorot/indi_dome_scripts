#!/usr/bin/python
#
# Park script for INDI Dome Scripting Gateway
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


try:
    coordinates = open('/tmp/indi-status', 'r')
    str = coordinates.readline()
    coordinates.close()
except:
    # Cannot read status file.
    sys.exit(1) 


if str[0] == '0':
    # Roof is already open
    sys.exit(0)


try:
    # Activate Relay
    GPIO.output(pin,False)
    time.sleep(1)
    #print "Disable..."
    GPIO.output(pin,True)

    # Time for the roo to open
    time.sleep(15)
except:
    GPIO.cleanup()
    sys.exit(1)


coordinates = open('/tmp/indi-status', 'w')
coordinates.truncate()
coordinates.write('0 0 0')
coordinates.close()

sys.exit(0)

