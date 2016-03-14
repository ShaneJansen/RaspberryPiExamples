#!/usr/bin/python
import RPi.GPIO as GPIO
import time

PIN_DEVICE = 4
PIN_PIR = 18
DEVICE_SHUTOFF = 120

# Vars
deviceOn = False
onTime = 0

# Init
GPIO.setmode(GPIO.BCM)

# Set pin mode/state
GPIO.setup(PIN_DEVICE, GPIO.OUT)
GPIO.output(PIN_DEVICE, GPIO.HIGH)
GPIO.setup(PIN_PIR, GPIO.IN)

# Main loop
try:
    while True:
        pir_output = GPIO.input(PIN_PIR)
        if pir_output == 1:
            print ("Motion detected")
            if deviceOn == False:
                print ("Turining on device")
                GPIO.output(PIN_DEVICE, GPIO.LOW)
                deviceOn = True
            onTime = time.time()
            time.sleep(3)
        if deviceOn == True and (onTime + DEVICE_SHUTOFF) < time.time():
            print ("Turing off device")
            GPIO.output(PIN_DEVICE, GPIO.HIGH)
            deviceOn = False
except KeyboardInterrupt:
  print("Quit via keyboard")
  GPIO.cleanup()
