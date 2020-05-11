# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes

lista = []
consoante = []
total = 0

for i in range(10):
	lista.append(input("Digite uma letra: "))
	if lista[i] not in ["a","e","i","o","u"]:
		consoante.append(lista[i]) 
		total += 1

print("você digitou um total de: ",total,"consoante,são elas: ",consoante)

"""
Pra facilitar esse programa foi utilizado o operador not in,ele basicamente vai verificar se o operando a sua esquerda
 não estar contido na lista a sua direita
 
"""