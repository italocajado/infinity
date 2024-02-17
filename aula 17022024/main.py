class Empregado():
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def vencimento():
        return 0.00
    
class Assalariado(Empregado):
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario
    
    def vencimento(self):
        return self.salario
    
class Horista(Empregado):
    def __init__(self, nome, sobrenome, cpf, precoHora, horasTrab):
        super().__init__(nome, sobrenome, cpf)
        self.precoHora = precoHora
        self.horasTrab = horasTrab
    
    def vencimento(self):
        valor = self.precoHora * self.horasTrab
        return valor

class Comissionado(Empregado):
    def __init__(self, nome, sobrenome, cpf, totalVenda, taxaComissao):
        super().__init__(nome, sobrenome, cpf)
        self.totalVenda = totalVenda
        self.taxaComissao = taxaComissao
    
    def vencimento(self):
        com = self.totalVenda * (self.taxaComissao/100)
        return com

print('Menu: ')

op = int(input('1 - Assalariado \n2 - Comissionado \n3 - Horista'))

if op == 1:
    nome = input('Informe o nome: ')
    sobrenome = input('Informe o sobrenome: ')
    cpf = input('Informe o cpf: ')
    salario = float(input('Informe o salario: '))
    func1 = Assalariado(nome, sobrenome, cpf, salario)
    print(func1.vencimento())
elif op == 2:
    nome = input('Informe o nome: ')
    sobrenome = input('Informe o sobrenome: ')
    cpf = input('Informe o cpf: ')
    totalVenda = float(input('Informe o total de vendas: '))
    comissao = float(input('Informe a comissão: '))
    func2 = Comissionado(nome, sobrenome, cpf, totalVenda, comissao)
    print(func2.vencimento())
elif op == 3:
    nome = input('Informe o nome: ')
    sobrenome = input('Informe o sobrenome: ')
    cpf = input('Informe o cpf: ')
    precoHora = float(input('Informe o preço/hora: '))
    horasTrab = float(input('Informe o total de horas trabalhadas: '))
    func3 = Horista(nome, sobrenome, cpf, precoHora, horasTrab)
    print(func3.vencimento())