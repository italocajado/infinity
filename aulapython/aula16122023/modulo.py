import math
import random
import datetime

def boasVindas(pessoa):
    print('ola', pessoa, 'seja, bem vindo(a)')

def mostrarCpf(nome, cpf, telefone):
    cadastro ={
        'Nome' : nome,
        'CPF' : cpf,
        'Telefone': telefone
    }
    print(cadastro['CPF'])

def soma(a,b):
    soma = a+b
    print('o resultado da soma é:', soma)

def peri(base, altura):
    area = base * altura
    perimetro = 2*(base + altura)
    diag = math.sqrt(base*base + altura*altura)
    print('A Area do triangulo é: ', area)
    print('A Diagonal do triangulo é: ', diag)
    print('O Perimetro do triangulo é: ', perimetro, 2)

def raizExa (n):
    if math.sqrt(n) == 2:
        print('o numero ', n, 'é uma raiz exata. ')
    else:
        print('não é raiz exata')

def raioCirc(r):
    A = math.pi * r**2
    print('A area do circulo é: ', A) 

def raiz(num):
    lista = []
    for num in range(5):
        num = int(input("Informe o numero: "))
        Rai = math.sqrt(num)
        lista.append(Rai)
    print('Raiz quadrada dos numero informados: ', lista)

def hipo(cat1, cat2):
    hipot = math.hypot(cat1, cat2)
    print("a hipotenusa: ", hipot)

def volCil(raio, altura):
    V = math.pi *(raio**2*altura)
    print(f'o volume de um cilindro de raio: {raio} e altura: {altura} é {V}')

def sorteio(pessoa):
    choice = random.sample(pessoa, 3)
    print(f'os ganhadores para o açai de 50, 30 e 20 KG respectivamente são {choice}')

def corretorData(d, m, a):
    mes = {
        '1': 'janeiro',
        '2': 'feveiro',
        '3': 'março',
        '4': 'abril',
        '5': 'maio',
        '6': 'junho',
        '7': 'julho',
        '8': 'agosto',
        '9': 'Setembro',
        '10': 'Outubro',
        '11': 'Novembro',
        '12': 'Dezembro'
    }