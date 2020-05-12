#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor
import math

a = []
elevacao = []
soma = 0

for i in range(5):
	a.append(float(input("Digite o valor do número %d:" %(i + 1))))
	soma += pow(a[i],2)
print(soma)

""" Nesse programa utilizamos o módulo math, e com ele foi possivel facilmente calcular a potencia utilizando a função pow(a,b)
mas também teria sido possivel utilizando o operador (**)
"""