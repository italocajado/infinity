#def soma (n1, n2):
#    soma = n1 + n2
 #   print(soma)

#soma(15,20)

#def salario (horas, valor_hora):
 #   salario = horas * valor_hora

  #  return salario

#comissao = float(input("digite a comissão: "))

#print (salario (160,44) * (1+(comissao/100)))

#def sub():
  #  n1 = float (input("digite o numero para subtrair: "))
    #n2 = float (input("digite outro numero: "))
    
   # print(n1 - n2)
#sub()

#def tempo(seg):
  #  hs = seg // 3600
   # seg -= hs * 3600
    #min = seg // 60
    #seg -= min * 60
    #print (f"{hs}:{min}:{seg}")

#seg = int(input("digite os segundos: "))    
#tempo(seg)

#def idade (an, dia, ms):
 #   d_ano = an * 365
  #  d_meses = an * 30
    
   # print (f"o total de dias é : {d_ano + d_meses + dia}")

#ano = int(input("digite sua idade: "))
#ms = int(input("digite seus meses: "))
#dia = int(input("digite os dias: "))

#idade(ano, ms, dia)

# def teste(n):
#     if n > 0:
#         print ("positivo")
#         
#         if n % 2 == 0:
#             print ("par")
#         else: 
#             print("impar")
#     else:
#         print ("negativo")# 

# num = (int(input("digite um numero: ")))# 

# teste(num)

# #def teste(n):
#     if n > 0:
#         print ("positivo")
#         
#         if n % 2 == 0:
#             print ("par")
#         else: 
#             print("impar")
#     else:
#         print ("negativo")# 

# num = (int(input("digite um numero: ")))# 

# teste(num)# 

import math

# def volume (R):
#   vl = (4 / (3 * math.pi) * (R ** 3))
#   print(vl)# 

# R = int(input ("Digite o raio: "))
# volume(R)

# def fat ():
#     n = int(input("digite o numero para ser o fatorial: "))
#     fato = 1
#     i = 2 
#     while i <= n :
#       fato = fato * i
#       i = i + 1
#     print(fato)# 

# fat() 

def mat (N):
    S = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/N
    print (S)

num = int(input("digite um valor para fazer as contas: "))
mat (num)