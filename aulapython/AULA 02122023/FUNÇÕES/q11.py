
def sub(frase, subs):
    return frase.replace(subs, '*')
    

frase = input('escreva qualquer coisa: ')
subs = input('qual letra irá sumir? ')
fraseNova = sub(frase, subs)
print(fraseNova)