lommepenger = 0             # variabel i heltall med 0 kroner på

print("Du har ",lommepenger, "kr fra før av")

har_du_rydda = input("Har du rydda rommet ditt? Svar j eller n: ")

if har_du_rydda == "j":     # du må ha dobbelt likhetstegn når du
                            # sjekker likheter etc
    lommepenger = lommepenger + 200
    
else:
    pass                     # funksjon som går videre

print("Du har ",lommepenger, "kr nå i lommepenger")

