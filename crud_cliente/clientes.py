from cProfile import label
import tkinter as tk
from tkinter import ttk
import re
import mysql.connector

    
#ttk
class App(tk.Tk): 

    def __init__(self):
        super().__init__()
        
        self.title("CRUD - Cliente")
        #label de Resultado
        self.varResultado = tk.StringVar(self)
        self.lblResultado = ttk.Label(
            self, textvariable=self.varResultado,
            font=("Arial", 18),
            background="#DDDDDD"
        )
        self.lblResultado.grid(row=0, column=0,columnspan=3,padx=20, pady=10, sticky="ewns")

        # label Nome
        self.lblNome = ttk.Label(
            self, text="Nome",
            font=("Arial", 16, "bold")
        )
        # chamada e posicionamento do label Nome
        self.lblNome.grid(row=1, column=0, sticky="w", padx=20, pady=5)
        # input Nome
        self.varNome = tk.StringVar(self)
        self.txtNome = ttk.Entry(
            self, textvariable=self.varNome,
            font=("Arial", 16)
        )
        self.txtNome.grid(row=1, column=1, sticky="we", padx=20, pady=5)
        self.txtNome.focus()

        # label E-mail
        self.lblEmail = ttk.Label(
            self, text="E-mail",
            font=("Arial", 16, "bold")
        )
         # chamada e posicionamento do label E-mail
        self.lblEmail.grid(row=2, column=0, sticky="w", padx=20, pady=5)
        # input Email
        self.varEmail = tk.StringVar(self)
        self.txtEmail = ttk.Entry(
            self, textvariable=self.varEmail,
            font=("Arial", 16)
        )
        self.txtEmail.grid(row=2, column=1, sticky="we", padx=20, pady=5)
        
        # Lista resultados
        # chamada e posicionamento da lista de clientes
        self.frameLista = ttk.Frame(self)
        self.frameLista.grid(row=3, column=0, columnspan=2, rowspan=4, sticky="nwes", padx=20, pady=10)

        self.txtLista = ttk.Treeview(
            self.frameLista, columns=('nome','email'),
            show="headings", height=7
        )
        self.txtLista.heading('nome', text='Nome')
        self.txtLista.heading('email', text='Email')

        def item_selected(event):
            for selected_item in self.txtLista.selection():
                item = self.txtLista.item(selected_item)
                record = item['values']
                self.varNome.set(record[0])
                self.varEmail.set(record[1])
        
        self.txtLista.bind('<<TreeviewSelect>>', item_selected)

        self.txtLista.grid(row=0, column=0, sticky="nwes")

        scrollbar = ttk.Scrollbar(
            self.frameLista, orient=tk.VERTICAL, 
            command=self.txtLista.yview)
        self.txtLista.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # Botões
        self.btnConectar = ttk.Button(
            self, text="Conectar",
            command=self.btnConectar_Click
        )
        self.btnConectar.grid(row=1, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)

        self.btnCriarTabela = ttk.Button(
            self, text="Criar tabela", 
            command=self.btnCriarTabela_Click           
        )
        self.btnCriarTabela.grid(row=2, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)

        self.btnInserir = ttk.Button(
            self, text="Incluir clientes",
            command=self.btnInserir_Click
            
        )
        self.btnInserir.grid(row=3, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)

        self.btnProcurar = ttk.Button(
            self, text="Listar clientes",
            command=self.btnListar_Click
            
        )
        self.btnProcurar.grid(row=4, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)

        self.btnEditar = ttk.Button(
            self, text="Atualizar dados",
            command=self.btnAtualizar_Click
            
        )
        self.btnEditar.grid(row=5, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)

        self.btnExcluir = ttk.Button(
            self, text="Apagar cliente",
            command=self.btnExcluir_Click            
        )
        self.btnExcluir.grid(row=6, column=2, sticky="nwes", padx=20, pady=5, ipadx=20)
      
        

#conexão
    def btnConectar_Click(self):
        try: 
            conexao = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = ""
            )
            mycursor = conexao.cursor()
            sql = "CREATE DATABASE IF NOT EXISTS crud_clientes"
            mycursor.execute(sql)
            self.varResultado.set("Conexão criada com sucesso!!")
            self.lblResultado.configure(background="#3cb371")
        except:
            self.varResultado.set("Erro ao criar conexão!!")
            self.lblResultado.configure(background="#ff6347")

#criar tabela
    def btnCriarTabela_Click(self):
        try:
            conexao = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "crud_clientes"
            )
            mycursor = conexao.cursor()
            sql = "CREATE TABLE IF NOT EXISTS clientes(nome VARCHAR(55) NOT NULL, email VARCHAR(255) NOT NULL, PRIMARY KEY (email))"
            mycursor.execute(sql)
            self.varResultado.set("Tabela criada com sucesso !")
            self.lblResultado.configure(background="#3cb371")
        except:
            self.varResultado.set("Erro ao criar Tabelas !!")
            self.lblResultado.configure(background="#ff6347")
        
#create
    def btnInserir_Click(self):
        nome = self.varNome.get().strip()
        email = self.varEmail.get().strip()

        reNome = re.fullmatch(r"\b[A-Za-z ]+\b", nome)
        reEmail = re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email)
                                             
        if reNome is None:
            self.varResultado.set("Por favor insira um Nome válido")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()
        elif reEmail is None:
            self.varResultado.set("Por favor insira um E-mail válido")
            self.lblResultado.configure(background="#FF9999")
            self.txtEmail.focus()
        else:
            try:
                conexao = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "crud_clientes"
            )
                mycursor = conexao.cursor()
                sql = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
                val = (nome, email)
                mycursor.execute(sql, val)
                conexao.commit()

                self.varResultado.set(str(mycursor.rowcount)+" registro inserido.")
                self.lblResultado.configure(background="#99FF99")
                self.varNome.set("")
                self.varEmail.set("")
                self.txtNome.focus()
            except:
                self.varResultado.set("Erro ao inserir novo registro.")
                self.lblResultado.configure(background="#FF9999")

            
    def btnListar_Click(self):
        self.txtLista.delete(*self.txtLista.get_children())
        try:
            conexao = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "crud_clientes"
            )
            mycursor = conexao.cursor()
            sql = "SELECT * FROM clientes ORDER BY nome ASC"

            if self.varNome.get() != "":
                sql = "SELECT * FROM clientes WHERE nome LIKE %s"
                val = (self.varNome.get(),)
                mycursor.execute(sql, val)
            elif self.varEmail.get():
                sql = "SELECT  * FROM clientes WHERE email LIKE %s"
                val = (self.varEmail.get(),)
                mycursor.execute(sql,val)
            else:
                mycursor.execute(sql)
            
            myresult = mycursor.fetchall()

            for contato in myresult:
                self.txtLista.insert('', tk.END, values=contato)
                
            self.varResultado.set("Registros encontrados com sucesso!!")
            self.lblResultado.configure(background="#99FF99")
            self.txtNome.focus()  
        except:
            self.varResultado.set("Erro ao buscar registros.")
            self.lblResultado.configure(background= "#FF9999")
#update
    def btnExcluir_Click(self):
        nome = self.varNome.get().strip()
        email = self.varEmail.get().strip()
        
        if nome =="" or email=="":
            self.varResultado.set("Selecione um registro para excluir.")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()
        else:
            try:
                conexao = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "crud_clientes"
                )
                mycursor = conexao.cursor()
                sql = "DELETE FROM clientes WHERE nome = %s AND email = %s"
                val = (nome, email)
                mycursor.execute(sql, val)
                conexao.commit()

                self.varNome.set("")
                self.varEmail.set("")

                self.btnListar_Click()
                self.varResultado.set("Registro deletado com sucesso!")
                self.lblResultado.configure(background="#3cb371")
            except:
                self.varResultado.set("Erro ao deletar o registro.")
                self.lblResultado.configure(background="#FF9999") 

    def btnAtualizar_Click(self):
        nome = self.varNome.get().strip()
        email = self.varEmail.get().strip()

        reNome = re.fullmatch(r"\b[A-Za-z ]+\b", nome)
        reEmail = re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email)

        if reNome is None:
            self.varResultado.set("O campo nome é obrigatório.")
            self.lblResultado.configure(background="#FF9999")
            self.txtNome.focus()
        elif reEmail is None:
            self.varResultado.set("Insira um email válido")
            self.lblResultado.configure(background="#FF9999")
            self.txtEmail.focus()
        else:        
            if len(self.txtLista.selection()) < 1:
                self.varResultado.set("Selecione um registro para editar.")
                self.lblResultado.configure(background="#FF9999")
                self.txtNome.focus()
                return       

            try:
                registro = self.txtLista.selection()[0]
                dadosRegistro = self.txtLista.item(registro)
                nomeRegistro = dadosRegistro["values"][0]
                emailRegistro = dadosRegistro["values"][1]

                conexao = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database = "crud_clientes"
                )
                mycursor = conexao.cursor()
                sql = "UPDATE clientes SET nome = %s, email = %s WHERE nome = %s AND email = %s"
                val = (nome, email, nomeRegistro, emailRegistro)
                mycursor.execute(sql, val)
                conexao.commit()

                self.varNome.set("")
                self.varEmail.set("")

                self.btnListar_Click()
                self.varResultado.set("Registro alterado com sucesso!!")
                self.lblResultado.configure(background="#3cb371")
            except:
                self.varResultado.set("Erro ao alterar registro.")
                self.lblResultado.configure(background="#FF9999")

if __name__ == "__main__":
    app = App()
    app.mainloop()