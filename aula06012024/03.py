
def calcTinta(lata, altura, largura):
    area = altura*largura
    totalLata = area / lata
    return totalLata

rend = float(input('Qual o rendimento da lata: '))
altura = float(input('informe a altura da parede: '))
largura = float(input('informe a largura da parede: '))

totalLata = calcTinta(rend, altura, largura)

print('Latas a serem usadas: ', totalLata)