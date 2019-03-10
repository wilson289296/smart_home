import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
if GPIO.input(5):
    GPIO.output(5, GPIO.LOW)
    print("RGB turned OFF.")
else:
    GPIO.output(5, GPIO.HIGH)
    print("RGB turned ON.")
