import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)

if GPIO.input(5):
    GPIO.output(5, GPIO.LOW)
    sleep(1)
    GPIO.output(8, GPIO.HIGH)
    sleep(0.2)
    GPIO.output(8, GPIO.LOW)
else:
    GPIO.output(5, GPIO.HIGH)
#    sleep(1)
#    GPIO.output(8, GPIO.HIGH)
#    sleep(0.2)
#    GPIO.output(8, GPIO.LOW)
