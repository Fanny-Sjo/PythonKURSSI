def suurin_arvo(a, b, c):
    suurin = a

    if b > suurin:
        suurin = b
    if c > suurin:
        suurin = c

    return suurin

luku1 = int(input("Anna eka luku: "))
luku2 = int(input("Anna toka luku: "))
luku3 = int(input("Anna kolmas luku: "))

#Pääohjelma
lopputulos = suurin_arvo(luku1, luku2, luku3)
print("Suurin annetuista luvuista on:", lopputulos)
