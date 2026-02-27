tunnus = input("Anna käyttäjätunnus: ")
salasana = input("Anna salasana: ")
yritykset = 0

while yritykset < 5:
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana, yritä uudelleen")
        yritykset += 1
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
if yritykset == 5:
    print("Pääsy evätty")

