from cProfile import label
from tkinter import *
import math

habili = []

def enviar():
    n1 = float(caixav1.get())
    n2 = float(caixav2.get())
    media = (n1+n2) / 2
    genero = radioVr.get()

    print('botão pressionado')
    print('Nome: ', caixa.get(),'\nIdade: ',caixa2.get())
    print(f'nota {media}')
    print('Genero: ', genero)

    if cc.get() == True:
        habili.append('C')
    if pyc.get() == True:
        habili.append('python')
    if jsc.get() == True:
        habili.append('Java Script')
    if outc.get() == True:
        habili.append('Outras')


    if media >= 7:
        print('APROVADO')
    else:
        print('REPROVADO')


janela = Tk()
janela.title('Cadastro de clientes')
janela.geometry("800x500+500+100")
janela.minsize(300, 200)
janela.maxsize(1000, 800)

nome = Label(janela, text='Informe seu nome: ',
fg='blue',
font=('Arial', 15, 'bold'))
caixa = Entry()

idade = Label(janela, text='Informe sua idade: ',
fg='blue',
font=('Arial', 15, 'bold')
)
caixa2 = Entry()

sex = Label(janela, text='Genero',
fg='blue',
font=('Arial', 15, 'bold'))

radioVr = StringVar()

genMasc = Radiobutton(janela, text='Masculino', variable=radioVr, value='Masculino')
genFem = Radiobutton(janela, text='Feminino', variable=radioVr, value='Feminino')
out = Radiobutton(janela, text='Outros', variable=radioVr, value='Outros')

cc = BooleanVar()
pyc = BooleanVar()
jsc = BooleanVar()
outc = BooleanVar()

hab = Label(janela, text='Habilidades',
            fg='blue',
font=('Arial', 15, 'bold'))

C = Checkbutton(janela, text='C', variable=cc)
Pyt = Checkbutton(janela, text='Python', variable=pyc)
Js = Checkbutton(janela, text='Java Script', variable=jsc)
outt = Checkbutton(janela, text='Outras', variable=outc)


v1 = Label(janela, text='Informe a primeira nota: ',
fg='blue',
font=('Arial', 15, 'bold'))
caixav1 = Entry()

v2 = Label(janela, text='Informe a segunda nota: ',
fg='blue',
font=('Arial', 15, 'bold')
)
caixav2 = Entry()

btn = Button(text='Enviar', command=enviar)

nome.place(x=1, y=50) 
caixa.place(x=200, y=55)
idade.pack()
caixa2.pack()
sex.pack()
genMasc.pack()
genFem.pack()
out.pack()
hab.pack()
C.pack()
Pyt.pack()
Js.pack()
outt.pack()
v1.pack()
caixav1.pack()
v2.pack()
caixav2.pack()
btn.pack()

janela.mainloop()