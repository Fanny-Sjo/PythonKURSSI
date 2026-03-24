import random

def heitto():
    return random.randint(1,6)

#Pääohjelma
while True:
    luku = heitto()
    print("Heitosta tuli", luku)

    if luku == 6:
        print("Ohjelma loppui")
        break
