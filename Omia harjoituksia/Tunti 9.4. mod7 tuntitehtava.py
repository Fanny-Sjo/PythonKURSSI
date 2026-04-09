hedelmien_hinnat = {"Bansku" : 1.0,
                    "Pärtsy" : 1.5,
                    "Omppu" : 2.0
                    }
yhteishinta = 0

while True:

    hedelma = input("Minkä hedelmän haluat (Bansku/Pärtsy/Omppu) (tyhjä lopettaa): ").capitalize() #tämä on avain
    if hedelma == "":
        print("Tilaus päättyy")
        break
    if hedelma in hedelmien_hinnat: #katsotaan onko annettu hedelmä meidän sanakirjassa
        print(f"{hedelma}n hinta on {hedelmien_hinnat[hedelma]}€")
        yhteishinta += hedelmien_hinnat[hedelma]
    else:
        print("Tuota hedelmää ei ole saatavilla.")
        lisataanko = input("Haluatko lisätä sen (Y/N)? ").upper()

        if lisataanko == "Y":
            hinta = float(input(f"Anna hinta {hedelma}lle: "))
            hedelmien_hinnat[hedelma] = hinta #viitataan sanakirjaan, annetaan uusi avain, asetetaan uusi arvo
            print(f"{hedelma} on lisätty hinnalla {hinta}")

print("Tilauksesi yhteihinta on", yhteishinta, "euroa.")

print("\nPäivitetty hinnasto: ")
for hedelma in hedelmien_hinnat:
    print(f"Hedelmä {hedelma}, hinta {hedelmien_hinnat[hedelma]}")
