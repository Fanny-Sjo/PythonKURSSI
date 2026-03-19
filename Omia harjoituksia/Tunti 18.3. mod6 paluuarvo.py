def neliosumma(a, b):
    _tulos = a**2 + b**2
    return _tulos

#Pääohjelma
luku1 = float(input("Anna eka luku: "))
luku2 = float(input("Anna toka luku: "))
tulos = neliosumma(luku1, luku2)

print(f"Lukujen {luku1} ja {luku2} neliösumma on {tulos}")