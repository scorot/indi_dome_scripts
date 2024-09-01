#!/usr/bin/python3
"""
This script open and close the rolloff roof indefinitely until the user
stops it by Ctrl+C.
"""
import sys
import os.path

import RPi.GPIO as GPIO
import time

motion_duration = 15
post_open_wait_time = 15
post_close_wait_time = 15

print("This script will open and close the rolloff roof indefinitely.")
print("Press Ctrl+C to stop.")
answer = input("Are you ok to proceed ? (press Y to proceed): ")
if answer != "Y":
    print("User asks to exit.")
    exit(0)

# CH1 -> pin 35
# CH2 -> pin 37
# CH3 -> pin 38
# CH4 -> pin 40
openpin = 35
closepin = 37

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(openpin, GPIO.OUT)
GPIO.setup(closepin, GPIO.OUT)


def open_door():
    pass

counter = 0
try:
    while(True):
        # Activate Relay to open
        print('Opening roof...')
        GPIO.output(openpin, False)
        time.sleep(1)
        ##print "Disable..."
        GPIO.output(openpin, True)

        # Wait for the roof to open
        time.sleep(motion_duration)
        print('Roof should be open.')
        print(f"Waiting {post_open_wait_time} seconds before closing...")
        time.sleep(post_open_wait_time)

        # Activate Relay to close the root 
        print('closing roof...')
        GPIO.output(closepin, False)
        time.sleep(1)
        ##print "Disable..."
        GPIO.output(closepin, True)

        # Wait for the roof to close
        time.sleep(motion_duration)
        print('Roof should be closed.')
        counter += 1
        print(f"Done {counter} cycles(s) so far.")
        print(f"Waiting {post_close_wait_time} seconds before new cycle...")
        time.sleep(post_close_wait_time)

except KeyboardInterrupt:
    print("Stop at user request.")
    print(f"Done {counter} cycles(s).")
    print("")
    GPIO.cleanup()
    sys.exit(0)

except Exception:
    GPIO.cleanup()
    sys.exit(1)

