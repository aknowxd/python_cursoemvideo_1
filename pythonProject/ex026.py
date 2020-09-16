frase = str ("Digite uma frase aew!").lower().strip()
count_a = frase.count("a")
a_pos = frase.find('a')+1
last_a = frase.rfind('a')+1

print(frase)
print("Quantidade de a: {}".format(count_a))
print("Primeira posicao do a: {}".format(a_pos))
print("Ultima posicao do a: {}".format(last_a))