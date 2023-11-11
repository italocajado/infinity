lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
listaPar = []
listaImpar = []

lista.reverse()
print('Lista reversa:\n',lista)

lista.sort()
print('Lista ordenada:\n',lista)

lista.append(27)
print('Lista com numero 27 ao final:\n',lista)

lista.remove(9)
print('Lista sem o numero 9:\n',lista)

del lista[10]
print('Lista sem a posição 10:\n',lista)


print('Lista somada:\n',sum(lista))

print(min(lista))
for valor in lista:
    if valor % 2 == 0:
        listaPar.append(valor)

print('numeros pares:\n', listaPar)    

for valor2 in lista:
    if valor2 % 2 != 0:
        listaImpar.append(valor2)

print('Numeros Impares:\n', listaImpar)

lista.insert(4, 89 )
lista.insert(5, 91)
print('lista com número 89 e 91 após o número 4:\n', lista)

print(len(lista))
