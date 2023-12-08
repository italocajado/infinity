saldo = float(input("Digite o saldo da conta: "))
correc = float(input("Qual a variação desse mes em %: "))

def rej(saldo, correc):
    return saldo * (correc/100) + saldo

correcao = rej(saldo, correc)
print('correção do mes R$ ', correcao)