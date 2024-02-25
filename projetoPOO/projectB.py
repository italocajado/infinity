from cProfile import label
import tkinter as tk
from tkinter import ttk

numero_membro = 1
catalogo = []

class Livro:
    def __init__(self, titulo, autor) -> None:
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        self.ID = 1

class Membro:
    def __init__(self, nome, numero) -> None:
        self.nome = nome
        self.numero = numero
        self.historico = []

class Biblioteca():

    def __init__(self) -> None:
        self.registro_membros = []

    def adicionar_membro(self):
        global numero_membro
        nome_membro = str(input("Digite o nome do membro: "))

        membro = Membro(nome=nome_membro, numero=numero_membro)
        numero_membro += 1
        self.registro_membros.append(membro)

    def emprestar_livro(self):
        pass

    def devolver_livro(self):
        pass

    def pesquisar_livro(self):
        pass


class App(tk.Tk, Biblioteca, Livro, Membro): 

    def __init__(self):
        super().__init__()
        
        self.title("Biblioteca")
        #self.iconbitmap("imagens/python.ico") 
        #label de Resultado
        self.varResultado = tk.StringVar(self)
        self.lblResultado = ttk.Label(
            self, textvariable=self.varResultado,
            font=("Arial", 18),
            background="#DDDDDD"
        )
        self.lblResultado.grid(row=0, column=0,columnspan=3,padx=20, pady=10, sticky="ewns")

        # label título
        self.lblTitulo = ttk.Label(
            self, text="Título",
            font=("Arial", 16, "bold")
        )
        # chamada e posicionamento do label título
        self.lblTitulo.grid(row=1, column=0, sticky="w", padx=20, pady=5)
        # input Título
        self.varTitulo = tk.StringVar(self)
        self.txtTitulo = ttk.Entry(
            self, textvariable=self.varTitulo,
            font=("Arial", 16)
        )
        self.txtTitulo.grid(row=1, column=1, sticky="we", padx=20, pady=5)
        self.txtTitulo.focus()

        # label autor
        self.lblAutor = ttk.Label(
            self, text="Autor",
            font=("Arial", 16, "bold")
        )
         # chamada e posicionamento do label E-mail
        self.lblAutor.grid(row=2, column=0, sticky="w", padx=20, pady=5)
        # input Email
        self.varAutor = tk.StringVar(self)
        self.txtAutor = ttk.Entry(
            self, textvariable=self.varAutor,
            font=("Arial", 16)
        )
        self.txtAutor.grid(row=2, column=1, sticky="we", padx=20, pady=5)
        
        # Lista resultados 

        

        

        # Botões
        self.btnCadastrar = ttk.Button(
            self, text="Cadastrar livro",
            command=self.btnInserir_Click
        )
        self.btnCadastrar.grid(row=1, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)

        self.btnMostrar = ttk.Button(
            self, text="Mostrar livros", 
            command=self.btnMostrar_Click        
        )
        self.btnMostrar.grid(row=2, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)

        self.btnEditar = ttk.Button(
            self, text="Editar livro",
            command=self.btnEditar_Click
            
        )
        self.btnEditar.grid(row=3, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)

        self.btnExcluir = ttk.Button(
            self, text="Excluir livro",
            command=self.btnExcluir_Click
            
        )
        self.btnExcluir.grid(row=4, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)

        self.btnEmprestar = ttk.Button(
            self, text="Emprestar livro",
            command=self.btnEmprestar_Click
            
        )
        self.btnEmprestar.grid(row=5, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)
        
   
    #métodos
    def btnInserir_Click(self):
        titulo = self.varTitulo.get()
        autor = self.varAutor.get()

        livro = Livro(titulo, autor)
        catalogo.append(livro)
        print(catalogo)
    

    def btnMostrar_Click(self):
        for i in catalogo:
            print(i.autor)

    def btnEditar_Click(self):
        pass

    def btnExcluir_Click(self):
        titulo = self.varTitulo.get()
        autor = self.varAutor.get()

        for i in catalogo:
            if titulo == i.titulo and autor == i.autor:
                catalogo.remove(i)
    
    def btnEmprestar_Click(self):
        titulo = self.varTitulo.get()
        autor = self.varAutor.get()

        for i in catalogo :
            if titulo == i.titulo and autor == i.autor and i.status == True:
                i.status = False
        

   
if __name__ == "__main__":
    app = App()
    app.mainloop()