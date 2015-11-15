import RPi.GPIO as GPIO
import thread
from time import sleep

sleep_time = 1

def watchInput():
    global sleep_time
    prev_input = 1
    while True:
        try:
            input = GPIO.input(23)
            if ((not prev_input) and input):
                sleep_time = sleep_time * 0.9
            prev_input = input
        except KeyboardInterrupt:
            break
                
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.IN)

thread.start_new_thread(watchInput, ())

green = False
while True:
    try:
        if (green):
            GPIO.output(17, GPIO.LOW)
            GPIO.output(22, GPIO.HIGH)
        else:
            GPIO.output(17, GPIO.HIGH)
            GPIO.output(22, GPIO.LOW)
        green = not green
        sleep(sleep_time)
    except KeyboardInterrupt:
        break

GPIO.output(17, GPIO.LOW)
GPIO.output(22, GPIO.LOW)

