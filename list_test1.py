# Mange greie og korte kommentarer som forklarer
# feks hva du gjør underveis
# feks hva funksjonene dine gjør
# feks at en liste er en datatype som kan innholde en lang rekke
# med data.
liste = [1,2,3,4,5,6]
print(liste)
liste.remove(2)  # tar bort et 2-tall hvis det er der
print(liste)
del liste[3]     # tar bort tallet på posisjon 3, som nå er 5 
print(liste)     # siden første plassen er 0, og andre er 1 osv.
liste.append(34) # legger til tallet 34 
liste.append(2)  # legger til tallet 2 tilslutt i lista
print(liste)
liste.sort()     # sorterer lista fra lavest til høyest
print(liste)
et_tall = int(input("Skriv inn et tall: ")) #input og gjør om til int.
liste.append(et_tall)  # legger tallet inn i lista
print(liste)
liste.sort()     # sorterer lista fra lavest til høyest
print(liste)

