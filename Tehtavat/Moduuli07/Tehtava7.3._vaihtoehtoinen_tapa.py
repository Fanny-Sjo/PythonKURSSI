lentoasemat = {
    "ABCD" : "Helsinki-Vantaa",
    "BCDE" : "Pariisi",
    "CDEF" : "Berliini"
}
 # Tässä mallissa tallennettu valmiiksi jo tietoja sanakirjaan kun läksyssä tein sanakirjan ensin tyhjäksi
while True:
    print("Valitse toiminto: A = SYÖTÄ, B = HAE, Q = LOPETA")
    valinta = input("Valitse toiminto: ")

    if valinta == "A":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.")

    elif valinta == "B":
        icao = input("Anna ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoaseman nimi on: {lentoasemat[icao]}")
        else:
            print("Koodia ei löydy tästä tiedostosta.")

    elif valinta == "Q":
        print("Ohjelma loppuu")
        break

    else:
        print("Virheellinen valinta")






























































