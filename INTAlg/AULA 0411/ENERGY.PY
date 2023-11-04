residencia = 0
comercial = 0
industrial = 0


tp1 = 0
tp2 = 0

while True:
    opcao = int(input("Digite a opção desejada:\n1 - Inserir Cliente\n2 - Encerrar \n"))
    if opcao == 1:
        nome = int(input("número do cliente: "))
        kw = float(input("Digite o consumo em Kw/Mes: "))
        codConsumidor = int(input("Qual o tipo de consumidor:\n1 - Residencial\n2 - Comercial \n3 - Industrial \n"))
        if codConsumidor == 1:
            residencia = kw + kw
            tp1 = tp1 + 1
            print(nome, " Cliente do tipo residencial, deverá pagar: R$ ", kw * 0.3)
        if codConsumidor == 2:
            comercial = kw + kw
            tp2 = tp2 + 1
            print(nome, " Cliente do tipo comercial, deverá pagar: R$ ", kw * 0.5)
        if codConsumidor == 3:
            industrial = kw + kw
            print(nome, " Cliente do tipo industrial, deverá pagar: R$ ", kw * 0.7)
    if opcao == 2:
        break



med = (comercial + residencia) / (tp1 + tp2)
print ("Total de consumo Residencial", residencia)
print ("Total de consumo Comercial", comercial)
print ("Total de consumo Industrial", industrial)
print ("Medias do tipo 1 e 2: ", med)