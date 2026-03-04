import math

while True:
    luku = int(input("Anna kokonaisluku: "))

    if luku == 0:
        print("poistuu loopista")
        break

    if luku  <0:
        print("Virheellinen numero")
    else:
             print(math.sqrt(luku))