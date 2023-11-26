#01;02
#eu = {
#    'nome' : 'italo',
#    'idade': 26,
#    'telefone': '85982169805',
#    'endereço' : 'Rua lourdes vidal alves, 716'
#}
#
#print(eu['nome'])

#03;04
#lista = {
#    'nome': input('digite seu nome:'),
#    'idade': int(input('Idade: ')),
#    'telefone': int(input('Digite o telefone: ')),
#    'endereço': input('Informe seu endereço: ')
#}
#print(lista)

#05
#tam = int(input("Informe o tamanho da sua agenda: "))
#agenda = {}
#
#for i in range(tam):
#    agenda.update({input('Digite o nome: ') : int(input('digite o telefone: '))})
#
#
#locate = input('Digite um nome para buscar: ')
#if locate in agenda:
#    print(agenda[locate])

#06
gp = {}

for i in range(3):
    nome = input('digite o nome: ')
    idade = int(input('Digite a idade: '))
    gp [f'grupo {i+1}'] = {
        'nome': nome,
        'idade': idade
    }

print(gp)