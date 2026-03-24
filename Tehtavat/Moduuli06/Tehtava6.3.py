def gallona_litroina(gallonat):
    return gallonat * 3.785

#Pääohjelma

while True:
    määrä = float(input("Kuinka paljon bensiiniä on gallonoissa? "))

    if määrä < 0:
        print("Ohjelma loppui")
        break

    litroina = gallona_litroina(määrä)
    print("Bensiiniä on", litroina, "litraa.")