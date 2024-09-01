#!/usr/bin/python
#
# Connect script for INDI Dome Scripting Gateway
#
# Arguments: none
# Exit code: 0 for success, 1 for failure
#

import sys
import os.path

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

state = True

if not os.path.exists('/tmp/indi-status'):
    try:
        coordinates = open('/tmp/indi-status', 'w')
        coordinates.truncate()
        coordinates.write('1 0 0')
        coordinates.close()
    except:
        # Cannot open status file
        time.sleep(2)
        sys.exit(1)

else:
    try:
        coordinates = open('/tmp/indi-status', 'r')
        status = coordinates.read().split(' ')
        coordinates.close()
        if len(status) == 3:
            print 'statut file exists and is ok'
            print 'status : {}'.format(status)
            sys.exit(0)
        else:
            print 'status file exists but is not ok'
            print 'status : {}'.format(status)
            sys.exit(1)
    except IOError:
        # Cannot open status file
        print 'Cannot open status file'
        time.sleep(2)
        sys.exit(1)

sys.exit(0)

