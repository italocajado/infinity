carros = {}
qtdeCar = int(input('informe quantos carros voce que adicionar: '))

for i in range(qtdeCar):
    nome = input('Digite o nome do carro: ')
    kmL = float(input('digite o km por litro: '))
    carros [f'carro {i+1}'] = {
        'nome': nome,
        'KM/L': kmL
    }

print(carros)
maior = 0
for c in carros:
    if carros[c['KM/L']] > maior:
        modelo = carros[c]['nome']
        maior = carros[c]['KM/L']

print('Modelo mais economico', modelo, 'fazendo', maior, 'Quilometros por litro')