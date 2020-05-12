# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos

idade = []
altura = []
media_altura = 0
conte = 0
 
for i in range (30):
	idade.append(int(input("Digite a idade do aluno %d:" %(i+1))))
	altura.append(float(input("Tambem digite a altura do aluno %d:" %(i+1))))
	media_altura += (altura[i])
print(media_altura)
for q in range(30):
	if ((idade[q] > 13) and (altura[q] < (media_altura/30))):
		conte += 1
	else:
		continue
print("A média da altura dos aluno é:",(media_altura/30),"E somente ",conte,"alunos com mais de 13 anos possivel altura menor que a média.")

