#Desenvolva um programa que pergunte a distancia de uma viagem em Km.
#Calcule o preco da passagem, cobrando RS 0.50 por KM para viagens de ate 200Km
#e RS 0.45 para viagens mais longas.

dist = int(input("Digite a distancia da viagem: "))
print("Sua viagem tem {}Km".format(dist))

if dist <= 200:
    v = dist * float(0.50)
    print("O valor da viagem custa {} reais".format(v))
else:
    v = dist * float(0.45)
    print("O valor da viagem custa {} reais".format(v))