class Human:
    def __init__(self, nome, idade, peso, sex):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.sex = sex

nome = input('Qual o seu nome: ')
age = input('Qual a sua idade: ')
peso = input('Qual o seu peso: ')
genero = input('Qual o seu genero: ')

h1 = Human(nome, age, peso, genero)

print(h1.nome, h1.idade, h1.peso, h1.sex)