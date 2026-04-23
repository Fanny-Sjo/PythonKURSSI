oppilaat = {"Saulus" : ["Saulus", 1, "Matikka"  ],
           "Valto" : ["Valto", 1,"Ohjelmointi"],
            "Oliver" :  ["Oliver", 2, "Viestintä"]
            }

print("Sauluksen vuosiluokka on",oppilaat["Saulus"][1])
print("Valton lempiaine on",oppilaat["Valto"][2])

oppilaat ["Valto"][2] = "Fysiikka"

oppilaat ["Anna"] = ["Anna", 3, "Välitunti"]

del oppilaat ["Saulus"]

print("\nLopullinen sanakirja: ")
print(oppilaat)