class Dog:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

nome = input('Qual o nome do seu doginho: ')
raca = input('Qual a raça dele: ')
idade = input('Qual a idade dele? ')

dog1 = Dog(nome, raca, idade)

print(dog1.nome, '-', dog1.raca, '-', dog1.idade)