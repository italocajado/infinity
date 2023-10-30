while True:
    opcao = int(input("Digite a opção desejada:\n1 - Inserir Cliente\n2 - Encerrar \n"))
    if opcao == 1:
        nome = int(input("número do cliente: "))
        kw = float(input("Digite o consumo em Kw/Mes: "))
        codConsumidor = int(input("Qual o tipo de consumidor:\n1 - Residencial\n2 - Comercial \n3 - Industrial \n"))
        if codConsumidor == 1:
            kw = kw * 0.3
            print(nome, " Cliente do tipo residencial, deverá pagar: R$ ", kw)
        if codConsumidor == 2:
            kw = kw * 0.5
            print(nome, " Cliente do tipo comercial, deverá pagar: R$ ", kw)
        if codConsumidor == 3:
            kw = kw * 0.7
            print(nome, " Cliente do tipo industrial, deverá pagar: R$ ", kw)
    elif opcao == 2 or nome == 0:
        break
