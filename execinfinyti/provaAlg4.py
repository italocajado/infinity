contador = 0

while True:
    num = int(input("Digite um numero: "))
    if num != 0:
        contador = contador + 1
    else:
        break
print(f"O total de vezes que um numero qualquer foi digitado foram {contador} vezes")
