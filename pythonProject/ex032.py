#Programa que leia um ano qualquer e mostre se ele e bissexto.

y = int(input("Digite um ano qualquer "))
if y%2 ==0 and y%100 != 0:
    print("Este ano e bissexto")
else:
    print("Este ano nao e bissexto")