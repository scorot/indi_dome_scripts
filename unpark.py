#!/usr/bin/python
#
# Park script for INDI Dome Scripting Gateway
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

try:
    coordinates = open('/tmp/indi-status', 'r')
    str = coordinates.readline()
    coordinates.close()
except:
    # Could not resd status file
    sys.exit(1)


if str[0] == '0':
    #print "Roof is already open/unparked."
    # Roof is already open
    time.sleep(2)
    sys.exit(0)

#time.sleep(2)
try:
    # Activate Relay
    GPIO.output(pin,False)
    time.sleep(1)
    GPIO.output(pin,True)

    coordinates = open('/tmp/indi-status', 'w')
    coordinates.truncate()
    # set 2 for dome in motion from closed to open
    # set 3 for dome in motion from open to closed
    coordinates.write('2 0 0')
    coordinates.close()

    # Time for the roof to open
    for i in range(15):    
        if os.path.exists('/tmp/indi-status-aborted'):
            time.sleep(1)
            #print "Unpark/Opening aborted."
            try:
            	os.remove('/tmp/indi-status-aborted')
                #print "Exiting."
                sys.exit(0)
            except:
                sys.exit(1)
        else:
	    time.sleep(1)

except:
    GPIO.cleanup()
    sys.exit(1)




coordinates = open('/tmp/indi-status', 'w')
coordinates.truncate()
coordinates.write('0 0 0')
coordinates.close()

sys.exit(0)

