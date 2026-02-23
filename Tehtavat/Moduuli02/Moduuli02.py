import math
name = input("Mikä on sinun nimesi? ")
print("Moi " + name)


r = float(input("Anna ympyrän säde: "))
print("ympyrän pinta-ala on: " + str(math.pi * r **2))

kanta = float(input("Mikä on suorakulmion kannan pituus? "))
korkeus = float(input("Mikä on suorakulmion korkeus? "))
print("pinta-ala: " + str(kanta * korkeus))
print("piiri: " + str(kanta *2 + korkeus*2))

luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))
print("summa: " + str(luku1 + luku2 + luku3))
print("tulo: " + str(luku1*luku2*luku3))
print("keskiarvo: " + str((luku1+luku2+luku3)/3))

luotigrammoina = 13.3
naulaluoteina = 32
leiviskanauloina = 20

leiviskat = float(input("Anna leiviskät "))
naulat = float(input("Anna naulat "))
luodit = float(input("Anna luodit "))

luodityht = float(leiviskat * leiviskanauloina * naulaluoteina + naulat * naulaluoteina + luodit)
grammatyht = float(luodityht * luotigrammoina)

kilogrammat = int(grammatyht/1000)
grammat = grammatyht%1000
print(str(kilogrammat) + "kg " + str(grammat) + "g")

