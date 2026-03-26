import math

luku = int(input("Anna luku väliltä 1-10: "))
for n in range(1,11):
    kertolaksu = luku * n
    print(f"{luku} * {n} = {kertolaksu}")


print("Tässä", luku,"kertotaulu")