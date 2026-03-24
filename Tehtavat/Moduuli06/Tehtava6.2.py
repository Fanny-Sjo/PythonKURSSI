import random

def heitto(tahkot):
    return random.randint(1, tahkot)

#Pääohjelma

tahkojen_määrä = int(input("Anna nopan tahkojen määrä: "))

while True:
    luku = heitto(tahkojen_määrä)
    print("Heitosta tuli", luku)

    if luku == tahkojen_määrä:
        print("Ohjelma loppui")
        break