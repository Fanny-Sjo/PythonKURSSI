viikko = ("ma", "ti", "ke", "to", "pe", "la", "su")

paiva = int(input("Anna viikonpäivän järjestysnumero (1-7): "))

vkpaiva = viikko[paiva -1]

print(f"{paiva}. päivä on {vkpaiva}.")

#-------------------
print("\nSeuraava harjoitus alkaa tästä!!!!!!")

hedelmat = ("Bansku", "Pärtsy", "Omppu")

(h1, h2, h3) = hedelmat #Muista tehdä näin päin, ei samoin päin kun ylempi

print("Hedelmä 1 on ", h1)
print("Hedelmä 2 on ", h2)
print("Hedelmä 3 on ", h3)

