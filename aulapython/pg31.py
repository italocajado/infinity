#08
lista1 = [10, 5 , 8, 9, 11, 1, 2, 3, 4, 5, 6, 7, 12, 13, 22]
chute = int(input('tente advinhar o numero: '))

for i in range(len(lista1)):
    if lista1[i] == chute:
        print('Acertou o numero: ', chute, 'esta na posição: ', i)
        break
else:
    print('errou') 
 
#09
lista2 = []
mult6 = []

for i in range(8):
    num = int(input('digite um valor: '))
    lista2.append(num)

for j in lista2:
    if j % 6 == 0:
        mult6.append(j)
print('multiplos de 6: ', mult6)

#10
alunos = []
med = []
sit1 = []
sit2 = []

for z in range(2):
    aluno = str(input('nome do aluno: '))
    nota1 = float(input('primeira nota: '))
    nota2 = float(input('segunda nota: '))
    media = (nota1 + nota2)/2
    med.append(media) #med injeta o valor da media do aluno na lista media
    alunos.append((aluno, media)) #alunos faz a injeção do nome do aluno(aluno) e da media (media) na lista alunos assumindo assim a seguintes posições alunos[[posição 0 = nome do alunos][posição 1 = media desse aluno]]
    
for k in range(len(alunos)):
    if alunos[k][1] > 7: #alunos [k = nome do alunos, posição[0]][1 = posição da nota]
        sit1.append(alunos[k])
    else:
        sit2.append(alunos[k])

print('alunos com a situação de aprovado', sit1)
print('alunos com a situação de reprovado: ', sit2)
