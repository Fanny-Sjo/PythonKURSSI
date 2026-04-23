import math

def create_point(x, y):
    return (x, y)

x1 = int(input("Anna pisteen x1 koordiaannti: "))
y1 = int(input("Anna pisteen y1 koordiaannti: "))
x2 = int(input("Anna pisteen x2 koordinaatti: "))
y2 = int(input("Anna pisteen y2 koordinaatti: "))

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

p1 = create_point(x1, y1)
p2 = create_point(x2, y2)

d = distance(p1, p2)

print(d)
