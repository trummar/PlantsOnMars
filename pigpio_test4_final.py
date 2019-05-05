import pigpio
from time import sleep
import RPi.GPIO as GPIO

#for å styre servo. pigpiod må kjøre på RPi.
#pigpio -V sjekker om du har installert. Følger med nyeste Raspian

pi = pigpio.pi()

#Her kan du selvsagt forandre pulslengden fra verdien 500-2500
#Pulsverdi 0 gir av
#

def servo_av():
    pi.set_servo_pulsewidth(18, 0)    # off
    sleep(1)
    
def servo_til_venstre():
    pi.set_servo_pulsewidth(18, 500)    # venstre max
    sleep(1)

def servo_i_midten():
    pi.set_servo_pulsewidth(18, 1680)    # midten
    sleep(1)

def servo_til_hoyre():
    pi.set_servo_pulsewidth(18, 2500)    # høyre max
    sleep(1)
    
def sjekke_GPIO_for_forandring(gpio_pinne):
    if GPIO.input(gpio_pinne):
            servo_til_venstre()
            print("vanning pågår")
    else:
            servo_i_midten()
            #for step in range(540,1740,100):
            #   pi.set_servo_pulsewidth(18, step)    # sakte tilbake
            #   sleep(0.5)
            print("Ikke vanning - vanning stoppes")

GPIO.setmode(GPIO.BCM)
gpio_pinne = 21
GPIO.setup(gpio_pinne, GPIO.IN)
GPIO.add_event_detect(gpio_pinne, GPIO.BOTH, bouncetime= 300)
GPIO.add_event_callback(gpio_pinne, sjekke_GPIO_for_forandring)



#løkke for å kjøre "evig"
while True:

   sleep(1)
   GPIO.setup(23, GPIO.OUT)     # for å kunne ha en LED blinkende for å se
   print("Led on")              # at loopen fungerer. 
   GPIO.output(23, GPIO.HIGH)
   sleep(1)
   print("LED off")
   GPIO.output(23, GPIO.LOW)
   servo_av()
   
