#!/usr/bin/python
#
# Abort script for INDI Dome Scripting Gateway
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
pinAbortOpen = 35
pinAbortClose = 37

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinAbortOpen, GPIO.OUT)
GPIO.setup(pinAbortClose, GPIO.OUT)

try:
    coordinates = open('/tmp/indi-status', 'r')
    str = coordinates.readline()
    coordinates.close()
except:
    # Could not resd status file
    sys.exit(1)


if str[0] == '2':
    # Roof is in motion from closed to open
    #print "Roof is in opening. Try to abort."
    try:
        # Activate Relay
        GPIO.output(pinAbortOpen,False)
        time.sleep(1)
        GPIO.output(pinAbortOpen,True)
        time.sleep(1)
        #print "Motion aborted."

    except:
 	#print "Failed to abort."
        GPIO.cleanup()
        sys.exit(1)

    try:
        #print "Write abortion file."
        abrtf = open('/tmp/indi-status-aborted', 'w')
        abrtf.close()
        sys.exit(0)
    except IOError:
        #print "Failed to write abortion file."
        sys.exit(1)



elif str[0] == '3':
    #print "Roof is in closing. Try to abort."
    try:
        # Activate Relay
        GPIO.output(pinAbortClose,False)
        time.sleep(1)
        GPIO.output(pinAbortClose,True)
        time.sleep(1)
        #print "Motion aborted."
    except:
	#print "Failed to abort."
        GPIO.cleanup()
        sys.exit(1)


    try:
        #print "Write abortion file."
        abrtf = open('/tmp/indi-status-aborted', 'w')
        abrtf.close()
        sys.exit(0)
    except IOError:
        #print "Failed to write abortion file."
        sys.exit(1)


else:
    #print "Roof is not in motion. Nothing to do."
    sys.exit(0)

