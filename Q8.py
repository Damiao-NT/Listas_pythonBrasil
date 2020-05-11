# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida


idade = []
altura = []

for i in range(2):
	idade.append(int(input("Digite a idade da pessoa %d: " %(i + 1))))
	for j in range(1):
		altura.append(float(input("tambem digite a altura da pessoa %d: " %(i + 1))))

idade.reverse()
print(idade)
altura.reverse()
print(altura)

""" Para facilitar esse programa utilizamos o método reverse(),com ele conseguimos imprimir a lista na ordem inversa