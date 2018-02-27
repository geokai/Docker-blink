"""Uses the GPIO library to access and control the io of the raspberry pi"""

import RPi.GPIO as GPIO
import time


# Configure the PIN 8:
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setwarnings(False)


# Blink Interval:
blink_interval = 0.5  # Seconds

# Blinker Loop:
while True:
    GPIO.output(8, True)
    time.sleep(blink_interval)
    GPIO.output(8, False)
    time.sleep(blink_interval)

# Release Resource:
GPIO.cleanup()
