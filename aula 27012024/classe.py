class Carro:
    def __init__(self, marca, modelo, ano, rodas, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.roda = rodas
        self.cor = cor

    def ligar(self):
        return f'O {self.modelo} esta ligado'
    
onix = Carro('GM', 'Onix PLus', '2021', True, 'Preto')
modelo = input('Informe o modelo do carro: ')
marca = input('Informe a marca do carro: ')
ano = input('Informe o ano do carro: ')
cor = input('Informe a cor do veiculo: ')
strada = Carro(marca, modelo, ano, True, cor)

print(onix.modelo)
print(onix.ligar())

print(strada.marca, ' - ', strada.modelo)
print(strada.ligar())

lista =[onix, strada]
print(lista[1].ano)

dic = {
    'carro1' : onix,
    'carro2' : strada
}

print(dic['carro1'].modelo)
print(dic['carro2'].ligar())