#q1
#n1 = int(input("Digite o primeiro valor: "))
#n2 = int(input("Digite o segundo valor: "))
#n3 = int(input("Digite o terceiro valor: "))
#
#maior = n1
#
#if n2 > maior:
#    maior = n2
#
#if n3 > maior:
#    maior = n3
#
#print("O maior número é: ", maior)

#q2
j1 = float(input("Digite os pontos do primeiro jogador: "))
j2 = float(input("Digite os pontos do segundo jogador: "))
j3 = float(input("Digite os pontos do terceiro jogador: "))

pontos = [j1, j2, j3]

min(pontos)

sum(pontos)

media = sum(pontos) / 3


if sum(pontos) > 100:
    print("A media de pontos do time foram: ", media)
else:
    print("Equipe desclassificada")

print("Números em ordem decrescente: ")

pontos.sort(reverse=True)
for pontos in pontos:
    print(pontos)