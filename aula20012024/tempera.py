from cProfile import label
from tkinter import *

def far():
    n1 = float(caixa.get())
    op = n1 * 1.8 + 32
    print('Temperatura de Celsius para Fahrenheit: ', op)

def cel():
    n1 = float(caixa.get())
    op = (n1 - 32) / 1.8
    print('Temperatura de Fahrenheit para Celsius', op)

janela = Tk()
janela.title('Conversor de temperatura')
janela.geometry("800x500+500+100")
janela.minsize(300, 200)
janela.maxsize(1000, 800)

celcius = Label(janela, text='Informe a temperatura : ',
fg='blue',
font=('Arial', 15, 'bold'))
caixa = Entry()

btn1 = Button(text='Cº para F', command=far)
btn2 = Button(text='F para Cº', command=cel)

celcius.pack()
caixa.pack()
btn1.pack()
btn2.pack()

janela.mainloop()