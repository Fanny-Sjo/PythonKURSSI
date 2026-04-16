lentoasemat = {}

while True:
    print("Valitse toiminto: \n1 = syötä uusi lentoasema \n2 = hae lentoaseman tiedot \n3 = lopeta")


    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.")

    elif valinta == "2":
        icao = input("Anna ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoaseman nimi on: {lentoasemat[icao]}")
        else:
            print("Koodia ei löydy tästä tiedostosta.")

    elif valinta == "3":
        print("Ohjelma loppuu")
        break

    else:
        print("Virheellinen valinta")