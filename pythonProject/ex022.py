name = str("Andre Luiz Pereira Oliveira")
upper = name.upper()
lower = name.lower()
count = len(name) - name.count(" ")
split = len(name.split()[0])

print("Seu nome eh: {}".format(name))
print("Nome com letras maisculas eh: {}".format(upper))
print("Nome com letras minusculas eh: {}".format(lower))
print("Quantidade de letras sem espaco: {}".format(count))
print("Quantidade de letras no primeiro nome: {}".format(split))