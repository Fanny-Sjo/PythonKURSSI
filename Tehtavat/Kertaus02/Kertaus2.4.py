def kuusi(koko):
    print("Tästä tulee hieno kuusi")

    for p in range(koko):
        pisteet = "*" *(2 * p + 1)
        valit = " " * (koko - p - 1)
        print(valit + pisteet)

    #jalka
    valit = " " * (koko - 1)
    print(valit + "*")

#Pääohjelma
kuusi(5)