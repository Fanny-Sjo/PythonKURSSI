
luku = int(input("Anna kokonaisluku "))
jakaja = 2
if luku <2:
    print("luku ei ole alkuluku")

else:

    while True:
        if jakaja == luku:
            print("luku on alkuluku")
            break

        if luku%jakaja==0:
            print("luku ei ole alkuluku")
            break

        else:
            jakaja+=1

