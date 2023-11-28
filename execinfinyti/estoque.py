estoque = {"tomate": [1000, 2.30],
	"alface": [500, 0.45],
	"batata": [2001, 1.20],
    "feijão": [100, 1.50]
}

while True:
    print('Bem vindo a budega do seu ze, escolha o que vai querer? ')
    pedido = int(input("\n 1 - Tomate \n 2 - Alface \n 3 - Batata \n 4 - Feijão \n 5 - Listagem das compras \n 6 - Encerrar\n"))
    if pedido == 1:
        print("Você escolheu tomates")
        qtdeTomate = int(input("Quantos você quer comprar? "))
        
        unidT = qtdeTomate * estoque['tomate'][1]
        abtT = estoque["tomate"][0] - qtdeTomate
        estoque["tomate"][0] = abtT
        
        print('Você comprou: ', qtdeTomate, 'de tomates')
        attT = qtdeTomate + qtdeTomate
        
        if qtdeTomate > estoque["tomate"][0]:
            print('Estoque insuficiente')
            break
        
    elif pedido == 2:
        print("Você escolheu alfaces")
        qtdeAlface = int(input("Quantas você quer comprar? "))
        unidA = qtdeAlface * estoque['alface'][1]
        
        abtA = estoque["alface"][0] - qtdeAlface
        estoque["alface"][0] = abtA
        
        print('Você comprou: ', qtdeAlface, ' de alfaces')
        attA = qtdeAlface + qtdeAlface
        
        if qtdeAlface > estoque["alface"][0]:
            print('Estoque Insuficiente')
            break
        
    elif pedido == 3:
        print("Você escolheu batatas")
        qtdeBatata = int(input("Quantas você quer comprar? "))
        unidB = qtdeBatata * estoque["batata"][1]
        
        abtB = estoque["batata"][0] - qtdeBatata
        estoque["batata"][0] = abtB
        
        print('Você comprou: ', qtdeBatata, ' de batatas')
        attB = qtdeBatata + qtdeBatata
        
        if qtdeBatata > estoque["batata"][0]:
            print('Estoque Insuficiente')
            break
        
    elif pedido == 4:
        print('Você escolheu Feijões')
        qtdeFeijao = int(input('Quantas você quer comprar? '))
        unidF = qtdeFeijao * estoque["feijão"][1]
        
        abtF = estoque["feijão"][0] - qtdeFeijao
        estoque["feijão"][0] = abtF
        
        print('voce comprou: ', qtdeFeijao, ' de feijão')
        attF = qtdeFeijao + qtdeFeijao
        
        if qtdeFeijao > estoque["feijão"][0]:
            print('Estoque insuficiente')
            break
        
    elif pedido == 5:
        print('suas compras até agora: ')
        print(attT, ' Tomates\n', attA, 'Alface\n', attB, ' Batatas\n', attF, ' Feijão')
        total = unidT + unidA + unidB + unidF
        print('Total das Compras R$ ', total)
        print(estoque)
        
    elif pedido == 6:
        break