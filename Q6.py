# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos 
# com média maior ou igual a 7.0

notas = []
for i in range(10):
    aluno = []
    for j in range(4):
        aluno.append(float(input('Informe a nota do aluno: %d' %(i + 1))))
    notas.append(aluno)

media = []
total = 0

for q in range(5):
	soma = 0
	for e in range(4):
		soma = (soma + notas[q][e])
		print(soma)
	media.append(soma/4)
	if (media[q] >= 7):
		total += 1
print(media)
print("Um total de ", total,"Tiverem media >= 7")







		 