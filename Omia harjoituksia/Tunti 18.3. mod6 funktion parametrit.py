def tervehdi(kerrat):
    for k in range(kerrat):
        print("Termosta")
    return

#Pääohjelma
print("Ohjelma alkaa")
tervehdi(3)
print("Ohjelma loppuu")
tervehdi(5)
print("Vielä kerran!")
tervehdi(1)

print("TOINEN HARJOITUS ALKAA TÄSTÄ")
#------------------------------

def tervehdi(tervehdys, kerrat):
    for k in range(kerrat):
        print(tervehdys)
    return

#Pääohjelma
print("Ohjelma alkaa")
tervehdi("Moikka",3)
print("Ohjelma loppuu")
tervehdi("Termosta", 2)
print("Vielä kerran!")
tervehdi("Hellou", 1)