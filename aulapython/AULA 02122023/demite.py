#10
funci = {}
lista = []

for j in range(3):
    admit = input("Insira o nome do funcionario: ")
    lista.append(admit)

funci['Funcionario'] = lista
print(funci)

demite = input('informe o numero atrbuido ao que deseja demitir: ')

funci['Funcionario'].remove(demite)

print(lista)
print(funci)