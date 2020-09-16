#Faca um programa que leia tres numeros e mostre qual e o maior e qual e o menor

n1 = input("Digite o primeiro numero: ")
n2 = input("Digite o segundo numero: ")
n3 = input("Digite o terceiro numero: ")

maior = n1

if n2 > maior:
    maior = n2

if n3 > maior:
    maior = n3

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print("Maior numero eh {}".format(maior))
print("Menor numero eh {}".format(menor))