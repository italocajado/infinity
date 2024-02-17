class Empresa():
    def __init__(self, cnpj, nome):
        self.cnpj = cnpj
        self.nome = nome
        self.lista = []

    def adicionar(self, funcionario):
        self.lista.append(funcionario)
    
    def remover(self, funcionario):
        for i in self.lista:
            if i.cpf == funcionario.cpf:
                self.lista.remove(funcionario)

    def listar(self):
        print('Funcionarios: ')
        for i in self.lista:
            print(i.nome)

class Funcionario():
    def __init__(self, nome, cpf, cargo, salario):
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario

print('Menu: ')

infinity = Empresa('000000000', 'infinity')

while True:
    op = int(input('1 - cadastrar \n2 - remover \n3 - listar \n4 - Encerrar \n'))
    if op == 1:
        nome = input('Informe o nome: ')
        cpf = input('Informe o cpf: ')
        cargo  = input('Qual o cargo: ')
        salario = float(input('Informe o salario: '))
        func = Funcionario(nome, cpf, cargo, salario)
        infinity.adicionar(func)
    elif op == 2:
        cpf = input('Informe o cpf a ser excluido: ')
        for func in infinity.lista:
            if func.cpf == cpf:
                infinity.remover(func)
                print('funcionario removido com sucesso. ')
                break
            else:
                print('Funcionario não encontrado')
    elif op == 3:
        print(infinity.listar())
    elif op == 4:
        break
    else:
        print("Opção invalida")
