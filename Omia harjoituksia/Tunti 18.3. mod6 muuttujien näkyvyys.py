def tervehdi(tervehdys, kerrat):
    for k in range(kerrat):
        print(tervehdys)
    return

#Pääohjelma
name = "Fanny"

tervehdi(name, 3)

#---------------
print("TOINEN HARJOITUS ALKAA TÄSTÄ")

def vaihda():
    kaupunki = "Vantaa"                      #Paikallinen muuttuja
    print("Funktion lopuksi: " + kaupunki)
    return

#Pääohjelma
kaupunki = "Helsinki"                        #Globaali muuttuja

print("Pääohjelmassa aluksi kaupunki on", kaupunki)
vaihda()
print("Pääohjelmassa lopuksi kaupunki on", kaupunki)