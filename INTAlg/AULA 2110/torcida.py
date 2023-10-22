i = 0
fortaleza = 0
ceara = 0
ferroviario = 0
icasa = 0
outros = 0

Fortaleza = 0
Caucaia = 0
Outros = 0
salario = 0

while i <= 10:
    time = int(input("Qual o seu time:\n1-Fortaleza\n2-Ceará\n3-Ferroviario\n4-Icasa\n5-Outros \n"))
    if time == 1:
        salario = float(input("Qual o seu salario ? "))
        fortaleza = fortaleza + 1
    elif time == 2:
        ceara = ceara + 1
        mora1 = input("onde voce mora:")
        if mora1 == "Fortaleza":
            Fortaleza = Fortaleza + 1
    elif time == 3:
        ferroviario = ferroviario + 1
        mora2 = input("onde voce mora: ")
        if mora2 == "Caucaia":
            Caucaia = Caucaia + 1
    elif time == 4:
        icasa = icasa + 1 
    elif time == 5:
        outros = outros + 1
    i += i + 1
    mediaFortSal = salario / fortaleza


print("Torcedores do Fortaleza", fortaleza)
print("Torcedores do Ceará: ", ceara)
print("Torcedores do Ferroviario: ", ferroviario)
print("Torcedores do Icasa: ", icasa)
print("Torcedores de outros times: ", outros)
print("Media salarial dos torcedores do fortaleza: ", mediaFortSal)
print("Moradores de Caucaia e torcedores do Ferroviario: ", Caucaia)
print("Moradores de Fortaleza e torcedores do Ceará: ", Fortaleza)