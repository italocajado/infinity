#09
misteryBox = {}

for i in range(4):
    coisa = input('informe o que voce quer inserar na caixa: ')
    misteryBox[f'{i+1}'] = coisa
    
print(misteryBox)

num = input('informe um numero: ')

if num in misteryBox:
    print(misteryBox[num])
else:
    print('não localizado')

