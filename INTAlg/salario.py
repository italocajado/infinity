#salario com descontos
hrTb = int(input("Quantas horas você trabalhou no mes? "))
slhr = int(input("Agora digite o quanto que você cobra por essas horas trabalhadas: "))

slbruto = hrTb * slhr
ir = slbruto * 0.11
inss = slbruto * 0.08
sindicato = slbruto * 0.05
total_descontos = ir + inss + sindicato
liquido = slbruto - total_descontos

print("O seu salario bruto esse mes foi de: R$ ", slbruto, " seus descontos são: \n R$ ", ir, " imposto de renda \n INSS: R$ ", inss,  " \n e por fim o sindicato dos Loops R$ ", sindicato, " \n totalizando assim R$ ", total_descontos, " \n ao fim de tudo isso, você irá receber R$ ", liquido)