vel = int(input("Qual a velocidade do carro? "))

if vel >= 81:
    print("Multado!")
    multa = (vel -80) * 7
    print("Valor da multa: {} reais".format(multa))
else:
    print("Nao foi multado")
