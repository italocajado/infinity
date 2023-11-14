lista = []
lista2 = []

for i in range(5):
    n = int(input("informe os valores: "))
    lista.append(n)

print(lista)

for j in range(10):
    m = int(input("informe os valores: "))
    lista2.append(m)

lista2.reverse()
print(lista2)

notas = []

for i in range(4):
    nota = float(input('Insira a nota do aluno: '))
    notas.append(nota)
    media = sum(notas)/len(notas)
print('Notas do aluno: ', notas)
print('Media do aluno: ', media)
idades = []

for i in range(20):
    idade = int(input("Digite a idade: "))
    idades.append(idade)
print('maior idade: ', max(idades))
print('Menor idade: ', min(idades))
letras = []

for i in range(10):
    letra = input('digite uma letra: ')
    letras.append(letra)
    
for j, p in enumerate(letras):
    print( + 1, '->', p)
    

q7 = []

for i in range(15):
    num = int(input('digite um numero: '))
    q7.append(num)
    
for k, z in enumerate(q7):
    print('Valor: ', k + 1, '->', z)