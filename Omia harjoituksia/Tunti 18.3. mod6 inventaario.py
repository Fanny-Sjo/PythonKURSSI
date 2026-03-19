def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat repussa: ")
    for t in tavarat:
        print("- " + t)
    tavarat.clear()
    return

#Pääohjelma
reppu = ["Taskulamppu", "Otsalamppu", "Pöytälamppu"]
inventaario(reppu)
reppu.append("Eväsleipä")
inventaario(reppu)

#------------------------
print("\nTOINEN HARJOITUS ALKAA TÄSTÄ")

def tervehdi(nimi):
    print(f"Tervehdys {nimi}!")
    return
def tervehdi_monesti(nimi, kerrat):
    while kerrat > 0:
        tervehdi(nimi)
        kerrat -= 1

#Pääohjelma
tervehdi_monesti("Fanny", 3)