import tkinter as tk

root = tk.Tk()

check = tk.BooleanVar()

checkBtn = tk.Checkbutton(root, text='Aceitar termos', variable=check)
naoaceitar = tk.Checkbutton(root, text='Não Aceitar termos', variable=check)

naoaceitar.pack()
checkBtn.pack()

radioVr = tk.StringVar()

radio1 = tk.Radiobutton(root, text='Opção 1', variable=radioVr, value='Opção 1')
radio2 = tk.Radiobutton(root, text='Opção 2', variable=radioVr, value='Opção 2')

radio1.pack()
radio2.pack()

root.mainloop()