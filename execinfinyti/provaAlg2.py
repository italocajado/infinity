km = float(input("Digite a velocidade do veiculo: "))
ex = km - 80
multa = ex * 20

if ex > 0:
    print("Multado, voce ultrapassou ", ex, " Km/h do permitido, sua multa sera de R$ ", multa, " Reais")
else:
    print("Voce esta dentro da velocidade permitida! Parabens.")
