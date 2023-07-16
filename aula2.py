# def jan (*args):
#     print(args)# 

#     soma = 0# 

#     for i in args:
#         soma += i
#     print (soma)# 

# jan (1,2,3,4)

# import math
# soma = lambda x: sum(x)
# 
# print (soma(range(1,math.pi, 1)))

# num = [1,2,3,4,5]# 

# quad = list(map(lambda x: x **2, num))# 

# print(quad)# 

# nome = "ItAlO"# 

# print(nome)# 

# nome = list(map(lambda x: x in ['a', 'e', 'i', 'o', 'u'], nome))# 

# print (nome)

# nome = "italo"# 

# vog = list(filter(lambda x: x in ["a", "e", "i", "o", "u"], nome))# 

# print (vog)

#for i in list(filter(lambda x: x % 11 == 2, range(1000, 2001, 1))):
 #   print(i)

#from functools import reduce#

#letras = ["i", "t", "a", "l", "o"]#

#nome = reduce(lambda x, y: x + y, letras)#

#print (nome)

#letras = ["italo", "joao", "mateus", "zacarias"]
#letras.sort(key=lambda letra: letra[1])

#print(letras)

# import math
# tempo = lambda seg: f"{seg // 3600}:  {(seg % 3600) // 60} : {(seg % 3600) % 60}
# print(tempo)
# 
# seg = int(input("digite os segundos: "))    
# tempo(seg)
# 
# contDias = lambda anos, meses, dias: (anos * 365) + (meses * 30) + dias
# 
# ano = int(input("digite seus anos: "))
# mes = int(input("digite os meses: "))
# dia = int(input("digite os dias: "))
# 
# print(contDias(ano, mes, dia))
#
#teste = lambda n: "positivo e par" if n > 0 and n % 2 == 0 else "negativo"
#
#num = int(input("digite um numero: "))
#print(teste(num))
