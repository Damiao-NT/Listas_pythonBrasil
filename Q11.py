# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada

primeira_lista = []
segunda_lista = []
terceira_lista = []
quarta_lista = []
for i in range(3):
	primeira_lista.append(float(input("Digite os elemntos da primeira lista: ")))
for j in range(3):
	segunda_lista.append(float(input("Digite os elementos da segunda lista: ")))
for q in range(3):
	terceira_lista.append(float(input("Digite os elementos da terceira lista: ")))
for e in range(3):
	quarta_lista.append(primeira_lista[q])
	quarta_lista.append(segunda_lista[q])
	quarta_lista.append(terceira_lista[q])
	
print(quarta_lista)