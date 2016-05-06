'''
Used for controlling a series of relays with a single
push button.  Each press of the button will turn on/off the corresponding
relay.  For example, 4 presses of the button will turn on/off relay 4.
'''

import RPi.GPIO as GPIO
import time

CONST_PIN_BUTTON = 26
CONST_PIN_RELAYS = [2, 3, 4, 17, 27, 22, 10, 9]
CONST_TIMEOUT = 1

# Init
GPIO.setmode(GPIO.BCM)
GPIO.setup(CONST_PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for i in CONST_PIN_RELAYS:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# Data
presses = 0
last_press = 0

# Main loop
while True:
    button_pressed = not(GPIO.input(CONST_PIN_BUTTON))
    if button_pressed == True:
        print("Button Pressed")
        presses = presses + 1
        last_press = time.time()
        time.sleep(0.2)
    if presses != 0 and time.time() - last_press > CONST_TIMEOUT:
        print("Execute " + str(presses) + " Presses")
        pin = CONST_PIN_RELAYS[presses - 1]
        state = GPIO.input(pin)
        if state == 1:
            GPIO.output(pin, GPIO.LOW)
        else:
            GPIO.output(pin, GPIO.HIGH)
        presses = 0
