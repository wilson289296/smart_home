import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
if GPIO.input(7):
    GPIO.output(7, GPIO.LOW)
    if GPIO.input(5):
	GPIO.output(5, GPIO.LOW)
else:
    GPIO.output(7, GPIO.HIGH)
    if not GPIO.input(5):
	GPIO.output(5, GPIO.HIGH)
