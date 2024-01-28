class Comp():
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.sal = salario

quadroFunc = []

for i in quadroFunc:
    print(i)

def excludeContato(nome):
    if nome in quadroFunc:
        quadroFunc.remove(nome)
    else:
        print("funcionario não localizado !!")


user = input('Qual o seu nome: ')
while True:
        opcao = int(input("Escolha uma opção: \n 1 - Adicionar Funcionario; \n 2 - Mostrar todos os Funcionarios; \n 3 - Excluir contato;  \n 4 - Sair; \n"))

        if opcao == 1:
             nome = input('Qual o nome do funcionario? ')
             cargo = input('Qual o cargo que ocupara? ')
             sal = input('Qual o salario? ')
             func = Comp(nome, cargo, sal)
             quadroFunc.append(func)
        elif opcao == 2:
         for i,p in quadroFunc:
            print(quadroFunc[i].nome)
        elif opcao == 3:
             nome = input('informe o nome para excluir: ')
             excludeContato(nome)
        elif opcao == 4:
             break
        else:
             print('Opção invalida')