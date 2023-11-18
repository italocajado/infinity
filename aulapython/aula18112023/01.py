#t = ()
#lista = list(t)
#
#qtde = int(input('quantos numeros: '))
#
#for i in range(qtde):
#    num = int(input('informe o numero: '))
#    if num % 2 != 0:
#        lista.append(num)
#
#for i in lista:
#    if i % 2 == 0:
#        lista.remove(i)
#t = tuple(lista)
#print(t)

#02
#p1 = ()
#lista1 = list(p1)
#p2 = ()
#lista2 = list(p2)
#
#notas = int(input('quantos alunos: '))
#
#for i in range(notas):
#    prova1 = float(input('insira as notas da prova1: '))
#    prova2 = float(input('insira as notas da prova2: '))
#    lista1.append(prova1)
#    lista2.append(prova2)
#
#mediaT1 = sum(lista1) / len(lista1)
#mediaT2 = sum(lista2) / len(lista2)
#
#if mediaT1 > mediaT2:
#    print('A melhor media foi a prova 1 com media: ', mediaT1)
#else:
#    print('A melhor media foi a prova 2 com media: ', mediaT2)

#03
l1 = ()
l2 = ()

lista1 = list(l1)
lista2 = list(l2)

qtd1 = int(input('qual o tamanho da tupla 1? '))

for i in range(qtd1):
    n = int(input('Informe o numero: '))
    lista1.append(n)

qtd2 = int(input('qual o tamanho da tupla 2? '))
for i in range(qtd2):
    n = int(input('Informe o numero: '))
    lista2.append(n)

l3 = tuple(lista1 + lista2)
lista3 = list(l3)
lista3.sort()
print('Tupla 3 em ordem crescente', lista3)
lista3.reverse()
print('Tupla 3 em ordem decrescente', lista3)
lista3 = tuple(l3)


    