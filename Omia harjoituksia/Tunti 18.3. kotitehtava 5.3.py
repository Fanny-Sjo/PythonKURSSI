#kotitehtävä 5.3. paremmin/toisella tavalla tehtynä

luku = int(input("Anna kokonaisluku "))
if luku <2:
    print("luku ei ole alkuluku")

else:
    jaollinen =  0

    for l in range(2, luku):
        if luku % l ==0:
            print(f"Luku on jaollinen {l} :llä")
            jaollinen += 1

    if jaollinen == 0:
        print("Luku on alkuluku")
    else:
        print("Luku ei ole alkuluku")