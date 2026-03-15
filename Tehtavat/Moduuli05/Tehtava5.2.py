import random

syote = (input("Anna luku: "))
luvut = list()


while True:
    if syote =="":
        break
    else:
        luku = int(syote)
        luvut.append(luku)
        syote = (input("Anna luku: "))

luvut.sort(reverse=True)
print("ohjelma loppui, viisi suurinta lukua ovat")
for luku in luvut [:5]:
    print(luku)