somaAtleta = 0
atletaPes = 0
atletaNovo = 100
pesoTot = 0
idadeTot = 0

for i in range(1, 13):
    nome = input("Qual o nome do atleta: ")
    idade = int(input("Idade do atleta: "))
    peso = float(input("Peso do atleta: "))
    if peso > atletaPes:
        atletaPes = peso
    pesoTot = peso + peso
    if idade < atletaNovo:
        atletaNovo = idade
    idadeTot = idade + idade
    i += 1 
    
medPeso = pesoTot / 12
medIdade = idadeTot / 12
print("Media de peso: ", medPeso)
print("Media de idade: ", medIdade)
print("O atleta mais novo tem", atletaNovo, " anos")
print("Atleta mais pesado: ", atletaPes, " Kgs")