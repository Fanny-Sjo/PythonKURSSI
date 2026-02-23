sukupuoli = input("Anna biologinen sukupuoli: ")
hemoglobiini = float(input("Anna hemoglobiini: "))
if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("hemoglobiini on alhainen")
    elif hemoglobiini <= 175:
        print("hemoglobiini on normaali")
    else:
        print("hemoglobiini on korkea")
elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("hemoglobiini on alhainen")
    elif hemoglobiini <= 195:
        print("hemoglobiini on normaali")
    else:
        print("hemoglobiini on korkea")
else:
    print("annettu virheellinen sukupuoli")