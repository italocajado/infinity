# i = 1
# 
# while i <= 6:
#     print("Italo cajado")
#     i += 1

#q1
#num = 1
#while num <= 50:
#    if num % 2 != 0:
#        print(num)
#    num += 1

#q2
#nome = input("digite seu nome:  ")
#senha = input("Digite sua senha: ")
#
#while nome == senha:
#    print("a senha não pode ser igual ao nome, informe a senha novamente")
#    senha = input("Digite sua senha: ")

# i=1
# soma = 0
# while i <= 5:
#     num = int(input("Digite um valor: "))
#     soma = soma + num
#     i += 1
# 
# media = soma / 5
# print("SOMA: ",soma)
# print("MEDIA: ",media)

i = 1
soma = 0
rep = 0
apr = 1
while i < 20:
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 7:
        apr = apr + 1
    elif nota < 7:
        rep = rep + 1
    soma = soma + nota
    i += 1

media = soma / 20
percRep = rep * 100

print ("Aprovados: ", apr)
print ("Reprovados: ", rep)
print ("Media da turma: ", media)
print ("Percentual reprovados: %", percRep/20)