n = input("Digite um numero: ")
nt = type(n)
nan = n.isalnum()
nal = n.isalpha()
nd = n.isdecimal()
nn = n.isnumeric()
nasc = n.isascii()

print("Type: {} AlphaNumerico: {} Decimal: {} Eh numerico: {} AscII: {}".format(nt, nan, nal, nd, nn, nasc))
