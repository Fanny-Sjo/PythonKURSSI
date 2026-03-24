def parittomat_pois(lista):
    uusi_lista = []

    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista

#Pääohjelma
luvut = [1, 2, 3, 4, 5 ,6, 7,8, 9, 10 ]

karsittu_lista = parittomat_pois(luvut)

print("Alkuperäinen lista: ", luvut)
print("Uusi lista, josta poistettu parittomat luvut: ", karsittu_lista)
