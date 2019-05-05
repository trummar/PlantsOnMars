
                           # biblioteket time. sleep(1) lar RPI
                            # vente 1 sekund før den går videre
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)      # Setter pinne-nummerering til BCM,
                         

GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.LOW)
GPIO.cleanup()
