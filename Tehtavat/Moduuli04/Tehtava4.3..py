syote = (input("Anna luku: "))
suurin = None
pienin = None

while True:
    if syote =="":
        break
    else:
        luku = int(syote)
        if suurin == None:
            suurin = luku
        if pienin == None:
            pienin = luku
        if luku > suurin:
            suurin = luku
        if luku < pienin:
            pienin = luku
        syote = (input("Anna luku: "))


print(f"ohjelma loppui, suurin on {suurin} , pienin on {pienin}")