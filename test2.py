import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.IN)

btnOn = False
prev_input = 1
while True:
    try:
        input = GPIO.input(23)

        if ((not prev_input) and input):
            btnOn = not btnOn
        prev_input = input

        if (btnOn):
            GPIO.output(17, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)
        else:
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)
    except KeyboardInterrupt:
        break

GPIO.output(17, GPIO.LOW)
GPIO.output(22, GPIO.LOW)

