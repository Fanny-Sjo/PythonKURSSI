
laskutoimitus = input("Anna haluamasi laskutoimitus (plus/miinus/kerto/jako)(, loppu lopettaa): ")

if laskutoimitus != "loppu":

    luku1 = int(input("Anna ensimmäinen luku: "))
    luku2 = int(input("Anna toinen luku:"))

    while True:
        if laskutoimitus == "plus":
            print(luku1 + luku2)
        elif laskutoimitus == "miinus":
            print(luku1 - luku2)
        elif laskutoimitus == "kerto":
            print(luku1 * luku2)
        elif laskutoimitus == "jako":
            print(luku1 / luku2)

        else:
            print("loppuu")
            break

        laskutoimitus = input("Anna haluamasi laskutoimitus (plus/miinus/kerto/jako): ")

        if laskutoimitus == "loppu":
            break
        luku1 = int(input("Anna ensimmäinen luku: "))
        luku2 = int(input("Anna toinen luku:"))
print("ohjelma loppuu")
