#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem
# ou nao formar um triangulo.

#formula ( b - c ) < a < b + c
#        (a - c ) < b < a + c
#        ( a - b ) < c < a + b


a = int(input("Digite o lado a: "))
b = int(input("Digite o lado b: "))
c = int(input("Digite o lado c: "))

va = ( b - c ) < a < b + c
vb = (a - c ) < b < a + c
vc = ( a - b ) < c < a + b

if va == True:
    if vb == True:
        if vc == True:
            print("Pode ser triangulo")
else:
    print("Nao pode ser triangulo")