from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title('Teste de combo Box')

diasSem = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo']

combBox = ttk.Combobox(janela, values=diasSem)
combBox.pack(padx=75, pady=20)

janela.mainloop()