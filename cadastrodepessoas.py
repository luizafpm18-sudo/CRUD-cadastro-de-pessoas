import sqlite3 as conector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb

class CadastroPessoas:
    def __init__(self, janela):
        self.estilo = ttk.Style()
        self.estilo.theme_use('alt')
        self.atualizar = False
        self.janela = janela

        self.estilo.configure('Excluir.TButton', background="#7A0808", foreground='white')
        self.estilo.configure('Atualizar.TButton', background="#A38D0C", foreground='white')
        self.estilo.configure('Novo.TButton', background="#57025F", foreground='white')
        self.estilo.configure('Salvar.TButton', background="#079107", foreground='white')
        self.estilo.configure('Anterior.TButton', background="#8B0E5E", foreground='white')
        self.estilo.configure('Proximo.TButton', background='#8B0E5E', foreground='white')

        self.paginaatual = 0
        self.qntdporpag = 38

        self.titulo_principal = tk.Label(
            self.janela, 
            text="CADASTRO DE PESSOAS", 
            font=("Arial", 16, "bold"), 
            foreground="#020B5F"
        )
        self.titulo_principal.pack(side=tk.TOP, pady=15)

        quadro_cima = tk.Frame(self.janela)
        quadro_cima.pack(side=tk.TOP, pady=5)


        self.quadro1 = tk.Frame(quadro_cima)
        self.quadro1.pack(side=tk.LEFT, pady=5)

        self.campoCPF = ttk.Label(self.quadro1, text="CPF")
        self.campoCPF.grid(column=0, row=0)
        self.preencheCPF = ttk.Entry(self.quadro1)
        self.preencheCPF.grid(column=1, row=0)

        self.campoNome = ttk.Label(self.quadro1, text="Nome")
        self.campoNome.grid(column=0, row=1)
        self.preencheNome = ttk.Entry(self.quadro1)
        self.preencheNome.grid(column=1, row=1)

        self.campoNascimento = ttk.Label(self.quadro1, text="Data de Nascimento")
        self.campoNascimento.grid(column=0, row=2)
        self.preencheNascimento = ttk.Entry(self.quadro1)
        self.preencheNascimento.grid(column=1, row=2)

        self.campoEmail = ttk.Label(self.quadro1, text="Email")
        self.campoEmail.grid(column=0, row=3)
        self.preencheEmail = ttk.Entry(self.quadro1)
        self.preencheEmail.grid(column=1, row=3)

        self.campoTelefone = ttk.Label(self.quadro1, text="Telefone")
        self.campoTelefone.grid(column=0, row=4)
        self.preencheTelefone = ttk.Entry(self.quadro1)
        self.preencheTelefone.grid(column=1, row=4)

        self.quadro2 = tk.Frame(quadro_cima)
        self.quadro2.pack(side=tk.LEFT, pady=5, padx=10)

        self.btnSalvar = ttk.Button(self.quadro2, text="Salvar", command=self.Salvar, style='Salvar.TButton')
        self.btnSalvar.grid(column=0, row=0)

        self.btnNovo = ttk.Button(self.quadro2, text="Novo", command=self.Novo, style='Novo.TButton')
        self.btnNovo.grid(column=1, row=0)

        self.btnAtualizar = ttk.Button(self.quadro2, text="Atualizar", command=self.PrincipalAtualizar, style='Atualizar.TButton')
        self.btnAtualizar.grid(column=0, row=1)

        self.btnDeletar = ttk.Button(self.quadro2, text="Excluir", command=self.ExcluirRegistro, style='Excluir.TButton')
        self.btnDeletar.grid(column=1, row=1)

        self.btn_anterior = ttk.Button(self.quadro2, text="◀ Anterior", command=self.pagina_anterior, style='Anterior.TButton')
        self.btn_anterior.grid(column=0, row=2)

        self.btn_proximo = ttk.Button(self.quadro2, text="Próximo ▶", command=self.pagina_proxima, style='Proximo.TButton')
        self.btn_proximo.grid(column=1, row=2)

        #criar tabela
        columns = ('CPF', 'nome', 'data_de_nascimento', 'email', 'telefone')
        self.tree = ttk.Treeview(janela, columns=columns, show='headings')

        #nome das colunas
        self.tree.heading('CPF', text='CPF')
        self.tree.heading('nome', text='Nome')
        self.tree.heading('data_de_nascimento', text='Data de nascimento')
        self.tree.heading('email', text='Email')
        self.tree.heading('telefone', text='Telefone')

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        
        self.Carregar()

    def PrincipalAtualizar(self):
        linhaselecionada = self.tree.item(self.tree.selection())
        CPF = str(linhaselecionada["values"][0]).zfill(11)

        conexao = conector.connect('Pessoal.db')
        cursor = conexao.cursor()
        comando = '''select CPF, nome, data_de_nascimento, email, telefone
        from cadastro_de_pessoas where CPF = ?'''
        cursor.execute(comando, (CPF, ))
        registro = cursor.fetchone()
        cursor.close()
        conexao.close()

        print(registro)
        self.preencheCPF.delete(0, tk.END)
        self.preencheCPF.insert('', registro[0])
        self.preencheCPF.config(state='disabled')

        self.preencheNome.delete(0, tk.END)
        self.preencheNome.insert('', registro[1])

        self.preencheNascimento.delete(0, tk.END)
        self.preencheNascimento.insert('', registro[2])

        self.preencheEmail.delete(0, tk.END)
        self.preencheEmail.insert('', registro[3])

        self.preencheTelefone.delete(0, tk.END)
        self.preencheTelefone.insert('', registro[4])

        self.atualizar = True

    def ExcluirRegistro(self):
        linhaselecionada = self.tree.item(self.tree.selection())
        CPF = str(linhaselecionada["values"][0]).zfill(11)

        conexao = conector.connect('Pessoal.db')
        cursor = conexao.cursor()
        comando = 'delete from cadastro_de_pessoas where CPF = ?'
        cursor.execute(comando, (CPF, ))
        conexao.commit()
        cursor.close()
        conexao.close()

        mb.showinfo(title="ATENÇÃO!", message="Cadastro excluido com sucesso.")

        self.Carregar()

    def Novo(self):
        #se apagar pra entender se é novo ou atualizar
        self.preencheCPF.config(state='normal')
        #apaga tudo pra fazer um novo
        self.preencheCPF.delete(0, tk.END)
        self.preencheNome.delete(0, tk.END)
        self.preencheNascimento.delete(0, tk.END)
        self.preencheEmail.delete(0, tk.END)
        self.preencheTelefone.delete(0, tk.END)

        self.atualizar = False

    def Salvar(self):
        conexao = conector.connect('Pessoal.db')
        cursor = conexao.cursor()

        if self.atualizar:
            comando = '''update cadastro_de_pessoas set nome = ?, 
            data_de_nascimento = ?, email = ?, telefone = ?
            where CPF = ?'''
            cursor.execute(comando, (self.preencheNome.get(), self.preencheNascimento.get(),
                                     self.preencheEmail.get(), self.preencheTelefone.get(), self.preencheCPF.get()))
        else:
            comando = '''insert into cadastro_de_pessoas (CPF, nome, data_de_nascimento, email, telefone)
            values(?, ?, ?, ?, ?)'''
            cursor.execute(comando, (self.preencheCPF.get(), self.preencheNome.get(), self.preencheNascimento.get(),
                                     self.preencheEmail.get(), self.preencheTelefone.get()))
        conexao.commit()
        cursor.close()
        conexao.close()
        mb.showinfo(title="SUCESSO!", message="Cadastro criado/atualizado com sucesso!")

        self.Carregar() 
        self.Novo()                     

    def Carregar (self):
        self.tree.delete(*self.tree.get_children())

        #sistema conta quantas linhas deve passar
        pular = self.paginaatual * self.qntdporpag

        conexao = conector.connect('Pessoal.db')
        cursor = conexao.cursor()
        comando = '''select CPF, nome, data_de_nascimento, email, telefone from cadastro_de_pessoas order by CPF asc LIMIT ? OFFSET ?'''
        cursor.execute(comando, (self.qntdporpag, pular))
        registros = cursor.fetchall()
        cursor.close()
        conexao.close()

        for registro in registros:
            self.tree.insert('', tk.END, values=registro)

        #Desativa o botão anterior se estiver na primeira página
        if self.paginaatual == 0:
            self.btn_anterior.config(state="disabled")
        else:
            self.btn_anterior.config(state="normal")
           
        #Desativa o botão próximo se a página atual trouxe menos registros que o limite
        if len(registros) < self.qntdporpag:
            self.btn_proximo.config(state="disabled")
        else:
            self.btn_proximo.config(state="normal")

    def pagina_anterior(self):
        if self.paginaatual > 0:
            self.paginaatual -= 1
            self.Carregar()


    def pagina_proxima(self):
        self.paginaatual += 1
        self.Carregar()