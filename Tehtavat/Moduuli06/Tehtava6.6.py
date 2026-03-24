import math

def yksikköhinta(halkaisija_sentit, hinta):
    säde_metreinä = (halkaisija_sentit / 2) / 100  # cm → m
    pinta_ala = math.pi * säde_metreinä ** 2
    return hinta / pinta_ala

#Pääohjelma

#Pizza1
halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija sentteinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))

#Pizza2
halkaisija2 = float(input("Anna toisen pizzan halkaisija sentteinä: "))
hinta2 = float(input("Anna toisen pizzan hinta euroina: "))


yksikköhinta1 = yksikköhinta(halkaisija1, hinta1)
yksikköhinta2 = yksikköhinta(halkaisija2, hinta2)

print("1. pizzan yksikköhinta on :", yksikköhinta1, "€ per neliömetri")
print("2. pizzan yksikköhinta on :", yksikköhinta2, "€ per neliömetri")

#verrataan pizzoja keskenään
if yksikköhinta1 < yksikköhinta2:
    print("\n 1. pizza antaa enemmän rahalle vastinetta")
elif yksikköhinta2 < yksikköhinta1:
    print("\n 2. pizza antaa enemmän rahalle vastinetta")
else:
    print("\n Pizzat ovat saman hintaiset")