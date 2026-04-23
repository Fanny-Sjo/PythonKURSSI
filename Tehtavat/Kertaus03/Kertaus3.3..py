kirjasto = { "ABC" : ["Mikael Agricola", 100, "alkukantainen teos"],
             "Harry Potter" : ["J.K Rowling", 2000, "fantasia"],
             "Erikoisjoukot" : ["Janne Lehtonen", 2025, "elämänkerta"]

}
print("Kirjoittaja",kirjasto["Erikoisjoukot"][0])
print("Genre",kirjasto["ABC"][2])

kirjasto ["Runokirja"] = ["Eino Leino", 1500, "runous"]

del kirjasto["Harry Potter"]

print("\n Päivitetty sanakirja: ")
print(kirjasto)