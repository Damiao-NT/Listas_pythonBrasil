# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores

numeros = []
par = []
impar = []
for i in range(20):
	numeros.append(int(input("Digite um número: ")))
	if (numeros[i] % 2 == 0):
		par.append(numeros[i])
	else:
		impar.append(numeros[i])

print("Os números digitados foram: ",numeros)
print("Os números pares são: ",par)
print("Os números impares são: ",impar)
