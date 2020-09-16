price = float(input("Digite o preco do produto: "))
discount = (5/100) * price
total = price - discount

print("O valor com desconto eh: {:.2f}".format(total))