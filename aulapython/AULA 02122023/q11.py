def sub(frase):
    frase.split()
    return frase

frase = []

inject = input('escreva qualquer coisa: ')
frase.append(inject)

cractere = input('informe o caractere para sumir: ')

print(frase.replace(cractere, '*'))