import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
if GPIO.input(7):
    GPIO.output(7, GPIO.LOW)
    print("Lamp is now off.")
else:
    GPIO.output(7, GPIO.HIGH)
    print("Lamp is now on.")
