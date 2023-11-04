notaEx = 0
notaRe = 0
notaBo = 0
SoEx = 0

for i in range(1, 11):
    idade = int(input("Idade: "))
    nota = int(input("Qual a sua nota?\n3 - excelente \n2- Bom \n1 - Regular "))
    if nota == 3:
        notaEx = notaEx + 1
        idEx = idEx
        + idade
        SoEx = SoEx + 1
    if nota == 2:
        notaBo = notaBo + 1
    if nota == 1:
        notaRe = notaRe + 1
    
medIdEx = idEx / SoEx
medBom = notaBo / 10

print ("Media de idade que votou excelente: ", medIdEx)
print ("Quantidade de pessoas que responderam regular: ", notaRe)
print ("Media das pessoas que votaram bom entre todos: ", medBom)