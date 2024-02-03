class Forma():
    def __init__(self, comp, altura, largura):
        self.comp = comp
        self.altura = altura
        self.largura =largura

class Circulo(Forma):
    def __init__(self, comp, altura, largura):
        super().__init__(comp, altura, largura)

    def area(self):
        ar = 3.14 * self.comp**2
        return f'Area do circulo {ar}'
    
    def perimetro(self):
        per = 2 * 3.14 * self.comp
        return f'Perimetro do circulo {per}'

class Ret(Forma):
    def __init__(self, comp, altura, largura):
        super().__init__(comp, altura, largura)
    
    def area(self):
        a = self.comp * self.altura
        return f'Area do retangulo {a}'

    def perimetro(self):
        per = 2*(self.comp+self.altura)
        return f'Perimetro do retangulo {per}'
    

c = Circulo(2, 4, 10)
ret = Ret(3, 6, 8)

print(c.area())
print(c.perimetro())
print(ret.area())
print(ret.perimetro())