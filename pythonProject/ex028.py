import random
n1 = random.randint(0,5)
n2 = int(input('Digite um numero: '))
print("O numero do computador foi {}".format(n1))
if n2==n1:
    print("Voce acertou! Parabens!")
else:
    print('Voce errou! Tente novamente!')


