tuumat = float(input("Anna mitta tuumissa ,negatiivinen lopettaa: "))
while tuumat >= 0:
    print(f"{tuumat} tuumaa on {2.54*tuumat} senttimetriä")
    tuumat = float(input("Anna mitta tuumissa, negatiivinen lopettaa: "))

print("Ohjelma loppui")