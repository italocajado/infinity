pesoPeixe = float(input("Digite aqui quantos quilos de peixe foram pegos: "))
es = pesoPeixe - 50 
multa = es * 4

if es > 0:
    print("O você Pescou demais!!, o excesso de peixe pescado foi de: ", es)
    print("Agora terá que pagar uma multa de R$ 4,00 por quilo pescado a mais, então o valor de sua multa sera de R$ ", multa, " reais.")
else:
    print('Parabéns! Você não pescou mais que 50kg')