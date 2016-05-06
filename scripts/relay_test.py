'''
Used for testing a series of relays by turning each on
in sequential order and then turning each off in sequential
order.
'''

import RPi.GPIO as GPIO
import time

CONST_SLEEP = 0.5
CONST_PINS = [2, 3, 4, 17, 27, 22, 10, 9]

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
