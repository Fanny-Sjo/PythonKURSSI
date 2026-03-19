#Tehtävä 1
def seven_brothers():
    veljekset.sort()
    print(veljekset)

#Pääohjelma
veljekset = ["Juhani", "Aapo", "Eero", "Lauri", "Simeoni", "Tuomas", "Timo"]
seven_brothers()
#----------------------------------------
print("\nTÄSTÄ ALKAA TOINEN TEHTÄVÄ")

#Tehtävä 2
def eka_kirjain(sana):
    print(sana[0])
    return

#Pääohjelma
eka_kirjain("python")
eka_kirjain("yellow")
eka_kirjain("tomorrow")
eka_kirjain("heliotrope")
eka_kirjain("open")
eka_kirjain("night")

#-----------------------------------------
print("\nTÄSTÄ ALKAA TOINEN TEHTÄVÄ")

#Tehtävä 3

def keskiarvo(_luku1, _luku2, _luku3):
    _tulos = (_luku1 + _luku2 + _luku3) / 3
    return _tulos




#Pääohjelma
luku1 = int(input("Anna eka luku: "))
luku2 = int(input("Anna toka luku: "))
luku3 = int(input("Anna kolmas luku: "))

tulos = keskiarvo(luku1, luku2, luku3)
print("Keskiarvo on: ", tulos)