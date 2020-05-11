
# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa

lista = []

for i in range(10):
	lista.append(int(input("Digite um número: ")))

lista.reverse()
print(lista)


"""
O valor de i é setado para o valor do primeiro elemento da lista (valor 0).
O código a ser repetido é executado.
O valor de i passa a se o valor do elemento seguinte da lista, se houver um próximo elemento. Se não houver, encerra a execução do for. Se houver, volta ao passo 2, com o valor de i já atualizado.

"""

"""
outra diga bastante importante é a do uso da função append que serve para adicionar elementos a lista

"""