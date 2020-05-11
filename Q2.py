
# Faça um Programa que leia 4 notas, mostre as notas e a média na tela


lista_notas = []

soma = 0
for i in range(4):
	print("Digite a",i + 1,"nota: ")
	lista_notas.append(float(input()))
	soma += lista_notas[i]
print("A sua média é: ", soma/4)





"""
Uma diga bastante importante é a do uso do método reverse() que serve para inverter os elementos de uma lista

"""