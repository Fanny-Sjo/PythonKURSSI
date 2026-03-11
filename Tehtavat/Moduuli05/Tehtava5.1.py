import random

arpakuutiot = int(input("Montako arpakuutiota? "))

summa = 0

for noppa in range(arpakuutiot):
    heitto = random.randint(1, 6)
    print(heitto)
    summa += heitto

print("Summaksi tuli", summa)




