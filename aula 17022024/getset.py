class Pessoa():
    def __init__(self, nome, cpf):
        self.nome = nome    #publico
        self.__cpf = cpf    #Privado
    
    def setcpf(self, cpf):
        self.__cpf=cpf
    
    def getcpf(self):
        return self.__cpf

pessoa1 = Pessoa('italo', '023')
print(pessoa1.nome)
print(pessoa1.getcpf())
pessoa1.setcpf('606')
print(pessoa1.getcpf())
        