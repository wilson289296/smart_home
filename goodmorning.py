import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
#7 = lamp, 8 = pc, 5 = rgb LED
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

if not GPIO.input(5):
    GPIO.output(5, GPIO.HIGH)
if not GPIO.input(7):
    GPIO.output(7, GPIO.HIGH)
GPIO.output(8, GPIO.HIGH)
sleep(0.2)
GPIO.output(8, GPIO.LOW)
