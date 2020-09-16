import math
cat_o = float(input("digite o cateto oposto: "))
cat_a = float(input("digite o cateto adjacente: "))
hip = math.hypot(cat_o , cat_a)

print("Hipotenusa eh: {}".format(hip))