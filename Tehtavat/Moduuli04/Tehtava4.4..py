import random

luku = random.randint(1, 10)
arvaus = int(input("Arvaa luku (1-10): "))

while arvaus != luku:
    if arvaus < luku:
        print("Liian pieni arvaus")
    if arvaus > luku:
        print("Liian suuri arvaus")
    arvaus = int(input("Arvaa luku (1-10): "))
print("Oikein")