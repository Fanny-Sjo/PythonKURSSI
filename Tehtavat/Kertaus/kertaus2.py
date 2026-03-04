tuntipalkka = float(input("Anna tuntipalkkasi: " ))
tehdyt_tunnit = float(input("Anna tehdyt-tunnit: " ))
viikonpäivä = input("Anna viikonpäivä: ")

if viikonpäivä == "sunnuntai":
    print("Päiväpalkka on:", tuntipalkka * 2 * tehdyt_tunnit)
else:
    print("Päiväpalkka on: ", tuntipalkka * tehdyt_tunnit, "euroa")