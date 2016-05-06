'''
Turns on or off relays via the terminal with
"on" and "off" commands.
'''

import RPi.GPIO as GPIO
import time

CONST_PINS = [4, 17, 2, 3, 20, 21]

# Init
GPIO.setmode(GPIO.BCM)

# Loop through pins and set mode/state
for i in CONST_PINS:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# Main loop
try:
    while True:
        command = input('Enter command: ').split()
        pin = int(command[0])
        state = command[1]
        if state == "on":
            GPIO.output(pin, GPIO.LOW)
        if state == "off":
            GPIO.output(pin, GPIO.HIGH)
    # Reset GPIO settings
    GPIO.cleanup()
    print("End of relay_control.py")
except KeyboardInterrupt:
  print("Quit via keyboard")
  GPIO.cleanup()
