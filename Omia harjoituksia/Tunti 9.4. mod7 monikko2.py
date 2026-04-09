import random

def heita():
    eka = random.randint(1,6)
    toka = random.randint(1,6)
    return (eka, toka)

noppa1, noppa2 = heita()
print(f"Heitit nopasta 1: {noppa1} ja nopasta 2: {noppa2}. Liiku siis yhteensä {noppa1+noppa2} askelta.")