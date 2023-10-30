massaIni = float(input("Digite a massa do material: "))
massa = massaIni
tempo = 0

while massaIni > 0.10:
    massaIni = massaIni - 0.25
    tempo = tempo + 30
    print(massaIni)
    
print("Para uma massa de: ", massa, " Kgs", "Levaria: ", tempo, " Segundos para que ela se torne menor que 0.10")

