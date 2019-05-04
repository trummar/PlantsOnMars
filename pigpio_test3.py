import pigpio
from time import sleep
import RPi.GPIO as GPIO

#for å styre servo. pigpiod må kjøre på RPi.
# kjøre sudo pigpiod - ellers får du kraftig beskjed om det. 
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
    pi.set_servo_pulsewidth(18, 1500)    # midten
    sleep(1)

def servo_til_hoyre():
    pi.set_servo_pulsewidth(18, 2500)    # høyre max
    sleep(1)

def servo_step(step):
    for i in range(500, step, 50):
        pi.set_servo_pulsewidth(18, i)
        sleep(0.2)
    servo_av()
    print("servo step-test ferdig")

sovetid = 1    
for i in range(1,3):
    servo_til_venstre()
    sleep(sovetid)
    servo_i_midten()
    sleep(sovetid)
    servo_til_hoyre()
    sleep(sovetid)
    print(i)

servo_av()
print("ferdig med testsyklus")

servo_step(2500)







