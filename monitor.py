import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.output(8, GPIO.HIGH)
sleep(0.2)
GPIO.output(8, GPIO.LOW)

