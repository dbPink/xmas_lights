import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.IN)

for num in range(1, 60):
    if (num % 2 == 0):
        GPIO.output(17, GPIO.LOW)
        GPIO.output(22, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)
    sleep(1)
