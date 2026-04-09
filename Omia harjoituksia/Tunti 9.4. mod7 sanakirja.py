numerot = {"Viivi" : "050",
           "Ahmed" : "040",
           "Pekka" : "030"
           }

numerot["Olga"] = "020"

for nimi in numerot:
    print(f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}")
 #OLE TARKKANA MIHIN VIITTAAT, VIITTAA ARVOON JOKA AVAIMEN KOHDALLA ON "NUMERO[NIMI]"