def laskettu_summa(luvut):

    summa = 0
    for l in luvut:
        summa += l
    return summa

#Pääohjelma
luvut = [1, 2, 3, 4, 5, 6, 7, 8]

tulos = laskettu_summa(luvut)
print("Listan yhteenlaskettu summa on: ", tulos)