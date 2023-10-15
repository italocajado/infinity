nome = (input("Informe o nome da pessoa: "))
idade = int(input("Agora digite a idade da pessoa: "))

if idade <= 10:
    print("Valor do plano de saude: R$ 30,00")
elif idade > 10 and idade <= 29:
    print("Valor do plano de saude: R$ 60,00")
elif idade > 29 and idade <= 45:
    print("Valor do plano de saude: R$ 120,00")
elif idade > 45 and idade <= 59:
    print("Valor do plano de saude: R$ 150,00")
elif idade > 59 and idade <= 65:
    print("Valor do plano de saude: R$ 250,00")
elif idade > 65:
    print("Valor do plano de saude: R$ 400,00")