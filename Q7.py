# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números

num = []
soma = 0
mult = 1
for i in range(5):
	num.append(int(input("Digite o valor do número %d:" %(i + 1))))
	soma += num[i]
	mult *= num[i] 

print("Os números digitados foram: ",num)
print("A adição dos números digitados é igual a: ",soma)
print("A multiplicação dos números digitados é igual a: ",mult)