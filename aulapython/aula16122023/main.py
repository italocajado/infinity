import modulo

nome = input('Qual o seu nome: ')
cpf = input('informe o CPF: ')
tel = input('informe o telefone')
n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))
modulo.boasVindas(nome)
modulo.mostrarCpf(nome, cpf, tel)
modulo.soma(n1, n2)

base = int(input('Informe a base do triangulo: '))
altura = int(input('Informe a altura do triangulo: '))

modulo.peri(base, altura)

num1 = int(input("Qual o numero para raiz exata: "))
modulo.raizExa(num1)

area = int(input("Informe o circulo do raio: "))
modulo.raioCirc(area)

rai = int(input("Informe o numero: "))
modulo.raiz(rai)

cat1 = int(input("Informe o cateto 1: "))
cat2 = int(input('informe o cateto 2: '))
modulo.hipo(cat1, cat2)

raio = float(input("informe o raio do cilindro: "))
altura = float(input("Informe o valor da altura: "))
modulo.volCil(raio, altura)

dia = int(input("Informe o dia de hoje: "))
mes = int(input("Informe o mes corrente: "))
ano = int()