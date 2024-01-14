from cProfile import label
from tkinter import *

def enviar():
    print('botão pressionado')

janela = Tk()
janela.title('Cadastro de clientes')
janela.iconbitmap('cliente.ico')
janela.geometry("800x500+500+100")
janela.minsize(300, 200)
janela.maxsize(1000, 800)

nome = Label(janela, text='Informe seu nome: ',
fg='blue',
font=('Arial', 15, 'bold'))
caixa = Entry()
btn = Button(text='Enviar', command=enviar)

email = Label(janela, text='Informe o email: ',
fg='blue',
font=('Arial', 15, 'bold')
)
caixa2 = Entry()


nome.pack()
caixa.pack()
email.pack()
caixa2.pack()
btn.pack()
janela.mainloop()