km = float(input("quantidade de KM percorridos: "))
dias = int(input("Informe a quantidade de dias alugado: "))
valor_dias = int(dias * 60)
valor_km = float(km * 0.15)

valor_total = valor_dias + valor_km
print("O valor a pagar e de R$ {:.2f}".format(valor_total))