import math
# a + b = c
cata = int(input("cateto adjacente: "))
catb = int(input("cateto oposto: "))
c = math.sqrt(math.pow(cata,2) + math.pow(catb,2))

print("Hipotenusa eh: {}".format(c))