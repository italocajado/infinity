from cProfile import label
from tkinter import *

def enviar():
    n1 = float(caixa.get())
    n2 = float(caixa2.get())
    soma = n1+n2
    print(soma)

janela = Tk()
janela.title('Calculadora')
janela.iconbitmap('calc.ico')
janela.geometry("800x500+500+100")
janela.minsize(300, 200)
janela.maxsize(1000, 800)

v1 = Label(janela, text='Informe o primeiro valor: ',
fg='blue',
font=('Arial', 15, 'bold'))
caixa = Entry()

v2 = Label(janela, text='Informe o segundo valor: ',
fg='blue',
font=('Arial', 15, 'bold')
)
caixa2 = Entry()

soma = Button(text='Somar', command=enviar)



v1.pack()
caixa.pack()
v2.pack()
caixa2.pack()
soma.pack()
janela.mainloop()