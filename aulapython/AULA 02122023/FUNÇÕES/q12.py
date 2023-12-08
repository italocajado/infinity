def busca(lista, locate):
    if locate in lista:
        return lista.index(locate)
    else:
        return -1

lista = []
tamLista = int(input('qual seria o tamanho da lista: '))

for i in range(tamLista):
    inject = int(input('Informe o valor: '))
    lista.append(inject)

locate = int(input("Qual o valor buscar na lista? "))
result = busca(lista, locate)
print(f'O numero: {locate} esta na posição: {result}')