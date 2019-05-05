import pigpio
from time import sleep
import RPi.GPIO as GPIO

#for å styre servo. pigpiod må kjøre på RPi.
#pigpio -V sjekker om du har installert. Følger med nyeste Raspian

pi = pigpio.pi()

def sjekke_GPIO_for_forandring(gpio_pinne):
    if GPIO.input(gpio_pinne):
            print("vann deteksjon")
    else:
            print("Ikke vann")

GPIO.setmode(GPIO.BCM)      # Setter GPIO-nummerering
gpio_pinne = 21             # Vi skal bruke GPIO til deteksjon
GPIO.setup(gpio_pinne, GPIO.IN) # gjør klar gpio-pinne 21 
GPIO.add_event_detect(gpio_pinne, GPIO.BOTH, bouncetime= 300)
                            # Dersom noe skjer....
GPIO.add_event_callback(gpio_pinne, sjekke_GPIO_for_forandring)
                            # ...så kalles funksjonen "sjekke_GPIO...."



   
