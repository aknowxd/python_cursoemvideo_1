#Crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome SANTO

city = (' belo horizonte ').strip()
cityfind = city.strip().split()[0].find('SANTO')

print("comeca com santo? {}".format(cityfind))