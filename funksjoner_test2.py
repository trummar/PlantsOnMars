import random as r              # importerer random-biblioteket
                                # slik at vi kan bruke funksjonen 
                                # randint() under som gir oss et 
                                # tilfeldig tall mellom 0 og bredde.

def tilfeldig(bredde):          # funksjonen ber om et tall "bredde"
    test = r.randint(0,bredde)  # Dette tallet brukes til å definere
                                # hvor mange forskjellige tall 
                                # tilfeldig kan være. 
    return test                 # returnerer variabelen til "tall"

tall = tilfeldig(13)            # lar variabelen tall få resultatet
                                # av å kjøre funksjonen "tilfeldig"
                                # med bredde = 13
print(tall)                     # printer resultatet
