class Conta:
    def __init__(self, nome, Cc, Ag, saldo):
        self.nome = nome
        self.Cc = Cc 
        self.Ag = Ag
        self.saldo = saldo
        self.cria = "03/02/2024"

    def sacar(self, valor):
        taxa = valor * 0.05
        self.saldo = self.saldo - valor - taxa
        return self.saldo
    
    def deposit(self, money):
        self.saldo = self.saldo + money
        return self.saldo
    
    def exsaldo(self):
        return f'O saldo em sua conta é: R$ {self.saldo}'
    
    def mostrar(self):
        return self.nome, self.Cc, self.Ag, self.cria


class ContaCorrente(Conta):
    def __init__(self, nome, Cc, Ag, saldo):
        super().__init__(nome, Cc, Ag, saldo)

    def sacar(self, valor):
        taxa = valor * 0.10
        self.saldo = self.saldo - valor - taxa
        return self.saldo
    
    def pagar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return f'Saldo apos pagamento do boleto R$ {self.saldo}'
        else:
            return 'Saldo insuficiente'

class Poupa(Conta):
    def __init__(self, nome, Cc, Ag, saldo):
        super().__init__(nome, Cc, Ag, saldo)
    
    def deposit(self, money):
        bonus = money*0.10
        self.saldo = self.saldo + money + bonus
        return self.saldo
    


nome = input('Qual o seu nome: ')
numero = input('Qual o numero da conta: ')
ag = input('Qual a agencia: ')
saldo = float(input('Qual o saldo da conta: '))

#conta1 = Conta(nome, numero, ag, saldo)

cc = ContaCorrente(nome, numero, ag, saldo)

#pp = Poupa(nome, numero, ag, saldo)

print(cc.mostrar())
print(cc.exsaldo())
print(cc.sacar(500))
print(cc.deposit(1000))
print(cc.pagar(350))
