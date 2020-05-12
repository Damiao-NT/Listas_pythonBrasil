#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores

primeira_lista = []
segunda_lista = []
terceira_lista = []

for i in range(10):
	primeira_lista.append(float(input("Digite os elemntos da primeira lista: ")))
for j in range(10):
	segunda_lista.append(float(input("Digite os elementos da segunda lista: ")))
for q in range(10):
	terceira_lista.append(primeira_lista[i])
	terceira_lista.append(segunda_lista[i])
print(primeira_lista)
print(segunda_lista)
print(terceira_lista)