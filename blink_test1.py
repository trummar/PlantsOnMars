from time import sleep      # Her importeres funksjonen sleep fra
                            # biblioteket time. sleep(1) lar RPI
                            # vente 1 sekund før den går videre
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)      # Setter pinne-nummerering til BCM,
                            # dvs GPIO nummer
GPIO.setwarnings(False)     # ta vekk advarsler om at porten er opptatt
GPIO.setup(23, GPIO.OUT)    # gjøre klar utgangen



   
while True:                 # Løkke for å kjøre inntil det bryter

   sleep(1)                 # vente 1 sekund
   print("Led on")
   GPIO.output(23, GPIO.HIGH)   # Åpne utgangen på GPIO23 slik at LED lyser
   sleep(1)
   print("LED off")
   GPIO.output(23, GPIO.LOW)     # stenge utgangen på GPIO23 slik at LED slukker

   if not KeyboardInterrupt:     # For å komme ut av loopen
      GPIO.cleanup()
      break                     # bryte 
   
