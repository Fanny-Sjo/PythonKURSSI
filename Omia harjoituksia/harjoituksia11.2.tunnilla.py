import random

print("Tämä on moduuli 02 tehtava 6")
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)

print("numerolukon koodi on: ", num1, num2, num3)

print("Tämä on moduuli 03 harjoituksia")
raha = float(input("Kuinka paljon sinulla on rahaa? "))
if raha >= 5:
    print("Voit ostaa kahvin!")
if raha < 5:
    print("Et saa kahvia")
print("Kiitos hei!")

pituus = float(input("Kuinka pitkä olet? "))
if 160 <= pituus < 180:
    print("Olet sopivan pituinen")

a = True
b = False

if a and b:
    print("Molemmat on totta")
if a or b:
    print("toinen on totta")
if not a and b:
    print("Kumpikaan ei ole totta")

numero = float(input("Anna joku numero "))

if numero > 0:
    print("Numero on positiivinen")
else:
    print("Numero on negativinen")

ika = int(input("Kuinka vanha olet? "))
if ika >= 65:
    print("Olet eläkkeellä")
elif ika >= 18:
    print("Olet työikäinen")
elif ika >= 7:
    print("Olet kouluikäinen")
else:
    print("Olet pieni lapsi")