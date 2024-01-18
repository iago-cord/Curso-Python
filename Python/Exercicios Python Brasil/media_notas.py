notas = []
while len(notas) < 4:
    nota = float(input('Digite as notas do aluno:'))
    notas.append(nota)
media_notas = 0
for nota_bim in notas:
    media_notas += nota_bim /4

print (media_notas)

