def somar(num1,num2):
    soma = num1 + num2
    return soma

def sub (num1, num2):
    sub = num1 - num2
    return sub

def mult(num1, num2):
    multi = num1 * num2
    return multi

def div(num1, num2):
    divi = num1 / num2
    return divi

num1 = float(input('informe o primeiro valor: '))
num2 = float(input('informe o segundo valor: '))

while True:
    opcao = int(input('Escolha a operação: \n 1 - Somar \n 2 - Subtração \n 3 - Multiplicar \n 4 - Dividir \n 5 - Encerrar'))
    if opcao == 1:
        print(somar(num1, num2))
    if opcao == 2:
        print(sub(num1, num2))
    if opcao == 3:
        print(mult(num1, num2))
    if opcao == 4:
        print(div(num1, num2))
    if opcao == 5:
        break