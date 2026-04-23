ihmiset = {
"John" : ["John", 30, "Engineer"],
"Emily" : ["Emily", 25, "Artist"],
"Anna" : ["Anna", 22, "Student" ]
}

print("Johnin nimi on ",ihmiset["John"][0] )
print("Johnin ikä on ",ihmiset["John"][1] )
print("Emilyn ammatti on ",ihmiset["Emily"][2] )

ihmiset ["Anna"][2] = "Opettaja"
print("Annan uusi ammatti ",ihmiset["Anna"][2] ) #varmistus

ihmiset ["James"] = ["James", 28, "kirjailija"]
print("James toimii",ihmiset["James"]) #varmistus

ihmiset ["Sophia"] = ["Sophia", 35, "lääkäri"]
print("Sophia toimii", ihmiset["Sophia"]) #varmistus

del ihmiset["Emily"]
for i in ihmiset.items():
    print(i) #näin saa kaikki allekkain, voisi myös vain print(ihmiset)

print("\nLopullinen sanakirja: ")
print(ihmiset)

