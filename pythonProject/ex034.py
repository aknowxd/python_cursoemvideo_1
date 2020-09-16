#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
#Para salario superiores a RS 1.250.00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento e de 15%.

sal = float(input("Digite o salario: "))
a_sup = (10 * sal) /100
a_inf = (15 * sal) /100

if sal >= 1251:
    print("seu aumento eh: {}".format(a_sup))

else:
    print("Seu aumento eh: {}12".format(a_inf))