
from ipaddress import collapse_addresses
from sqlite3 import Row
from tkinter import *
from tkinter.tix import COLUMN

def enviar():
    print('botão pressionado')

janela = Tk()
janela.title('arvore')
janela.iconbitmap('pessoas.ico')
janela.geometry("800x500+500+100")
janela.minsize(300, 200)
janela.maxsize(1000, 800)
janela.configure(background='grey')

btn1 = Button(text='1', command=enviar)
btn2 = Button(text='2', command=enviar)
btn3 = Button(text='3', command=enviar)
btn4 = Button(text='4', command=enviar)
btn5 = Button(text='5', command=enviar)
btn6 = Button(text='6', command=enviar)






btn1.grid(column=3, row=0)
btn2.grid(column=2, row=1, columnspan=2)
btn3.grid(column=3, row=1, columnspan=2)
btn4.grid(column=2, row=2)
btn5.grid(column=3, row=2)
btn6.grid(column=4, row=2)
janela.mainloop()