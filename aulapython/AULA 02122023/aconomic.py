def desconto(n, desc):
    desco = n * desc/100
    valfinal = n - desco
    return valfinal

n = int(input("informe o valor do produto: "))
desc = float(input('informe a porcentagem de desconto: '))

print('O novo valor do produto, antes por: R$ ', n, 'Agora está por: R$ ', desconto(n,desc))