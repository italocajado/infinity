cliente = {
    'nome' : 'italo',
    'idade' : 26,
    'endereco' : 'rua lourdes vidal alves, 716'
}

capitais ={
    'Brasil' : 'Brasilia',
    'Reino Unido' : 'Londres',
    'Russia' : 'Moscow',
    'China' : 'Hong Kong',
    'Alemanha' : 'Berlin'
}

paisDg = input('informe um pais: ')

if paisDg in capitais:
    print('pais existe', capitais[paisDg])
else:
    print('pais não existe! ')