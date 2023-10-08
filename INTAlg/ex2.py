#dados
nome = input("Qual o seu nome: ")
adress = input("Endereço de residencia: ")
tel = int(input("Qual o seu telefone: "))

print("Olá, ", nome, ", vi que você reside em:", adress, " e seu telefone é: ", tel, " sera um prazer atende-lo. :)")

#media float
n1 = float(input("digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
n3 = float(input("Digite o terceiro valor: "))
media = n1+n2+n3 / 3

print("A media é: ", media)

#4 operações
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

soma = num1+num2
sub = num1-num2
prod = num1*num2
div = num1/num2

print ("As quatro operações para os numeros: ", num1, "e", num2, "são: produto ", prod, " soma: ", soma, " subtração: ", sub, " e divisão: ", div)

#conversor de moeda
dollar = float(input("digite o valor que deseja converter em dolares: "))
conv = dollar*4.90

print("A quantia de dolares digitadas foi: ", dollar, " e a conversão para reais R$ é de: ", conv)