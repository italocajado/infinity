def media(n1, n2, n3):
    med = (n1+n2+n3) / 3
    return med


qtdeProva = int(input('informe a quantidade de alunos: '))
for i in range(qtdeProva):
    n1 = float(input('nota da primeira prova: '))
    n2 = float(input('nota da segunda prova: '))
    n3 = float(input('nota da terceira prova: '))
    print(f'media do aluno numero: ${i+1} ', media(n1,n2,n3))
