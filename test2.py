

from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO
import time

myGPIO=18
myServo = Servo(myGPIO)

def callback(channel):
    if GPIO.input(channel):
            print("LEd off")
    else:
            print("LED on")

GPIO.setmode(GPIO.BCM)
channel = 21
GPIO.setup(channel, GPIO.IN)
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime= 300)
GPIO.add_event_callback(channel, callback)


print("Using GPIO17")
print("Using Gpiozero defaults for the servo class")

while True:
        
  #myServo.mid()
  #print("Set to middle position")
  sleep(1)
  myServo.min()
  print("Set to minimum position")
  sleep(1)
  #myServo.mid()
  #print("Set to middle position")
  #sleep(1)
  myServo.max()
  print("Set to maximum position")
  sleep(1)
