#!/usr/bin/python
import RPi.GPIO as GPIO
import time

CONST_SLEEP = 2
CONST_PINS = [4, 17, 2, 3, 20, 21]

# Init
GPIO.setmode(GPIO.BCM)

# Loop through pins and set mode/state
for i in CONST_PINS:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# Main loop
try:
    # Turn on the relays
    for index, item in enumerate(CONST_PINS):
        time.sleep(CONST_SLEEP)
        GPIO.output(item, GPIO.LOW)
        print("RELAY " + str(index + 1) + " IS ON")
    # Turn off the relays
    for index, item in enumerate(CONST_PINS):
        time.sleep(CONST_SLEEP)
        GPIO.output(item, GPIO.HIGH)
        print("RELAY " + str(index + 1) + " IS OFF")
    # Reset GPIO settings
    GPIO.cleanup()
    print("End of relay.py")
except KeyboardInterrupt:
  print("Quit via keyboard")
  GPIO.cleanup()
