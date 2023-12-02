def copiar(lista):
    lista2 = lista.copy()
    lista2.sort()
    return lista2

lista = []
tamLista = int(input('qual seria o tamanho da lista: '))

for i in range(tamLista):
    inject = int(input('Informe o valor: '))
    lista.append(inject)


print('copia da lista principal: ', copiar(lista))
