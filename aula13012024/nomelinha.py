
from ipaddress import collapse_addresses
from tkinter import *
from tkinter.tix import COLUMN

def enviar():
    print('botão pressionado')

janela = Tk()
janela.title('Cadastro de clientes')
janela.iconbitmap('pessoas.ico')
janela.geometry("800x500+500+100")
janela.minsize(300, 200)
janela.maxsize(1000, 800)
janela.configure(background='grey')

nome = Label(janela, text='Informe seu nome: ',
font=('Arial', 15, 'bold'))

caixa = Entry()

nome.configure(background='grey')
btn = Button(text='Confirmar', command=enviar, background='green')






nome.grid(column=0, row=0, pady=200)
caixa.grid(column=1, row=0)
btn.grid(column=2, row=0)
janela.mainloop()