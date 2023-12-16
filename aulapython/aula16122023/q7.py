import modulo

numeroCandidatos = int(input("Informe o numero de cadidatos: "))
lista = []
for i in range(numeroCandidatos):
    pessoa = input("Digite o nome do candidato: ")
    lista.append(pessoa)


modulo.sorteio(lista)