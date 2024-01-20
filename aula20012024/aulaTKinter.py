from tkinter import *

janela = Tk()
janela.title('Tkinter aula 2')
janela.geometry('600x400+200+100')

frame = Frame(janela,
              width=200,
              height=200,
              bg='green',
              borderwidth=2,
              relief='flat'
              )

frame.pack(side='left')
janela.mainloop()