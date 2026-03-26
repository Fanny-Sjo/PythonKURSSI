lista = []

while True:
    arvo = int(input("Anna luku: "))

    if arvo == 0:
        print("Ohjelma loppui")
        break

    lista.append(arvo)

    print("Lista annetuista luvuista: ", lista)
    print("Lista suuruusjärjestyksessä: ", sorted(lista))