alder = int(input("Hvor gammel er du? "))

if alder <= 12:
    print("Du går nok på barneskolen")
    
elif (alder > 12) and (alder <= 16):
    print("kanskje du går på ungdomsskolen")

elif (alder > 16) and (alder <= 19):
    print("kanskje du går på VGS")
    
else:
    print("Hmmm går du egentlig på skolen?")

    
