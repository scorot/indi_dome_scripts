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

state = True

# endless loop, on/off for 1 second
try:
    while True:
        print "Activate..."
        GPIO.output(pin,True)
        time.sleep(3)
        print "Disable..."
        GPIO.output(pin,False)
        time.sleep(3)
except KeyboardInterrupt:
   GPIO.cleanup()
   print "Exiting..."
   exit()

