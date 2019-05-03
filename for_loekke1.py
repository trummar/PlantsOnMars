liste1 = []               # Lager en liste klar.

for i in range(1,10):     # teller 9 ganger, fra 1 til men ikke 10
    data = int(input("Gi meg et tall: ")) # få input fra bruker
    liste1.append(data)   # legge tallet du fikk i en liste
    print(liste1)         # printe lista så lang den er nå
print(liste1)             # printe resultatet til slutt

