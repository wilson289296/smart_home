import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
#lamp and computer rgb
GPIO.output(7, GPIO.LOW)
GPIO.output(8, GPIO.HIGH)
sleep(0.2)
GPIO.output(8, GPIO.LOW)
