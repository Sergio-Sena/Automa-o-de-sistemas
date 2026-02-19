import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class SistemaCompleto:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Login e Cadastro")
        self.root.geometry("900x700")
        self.root.configure(bg='#2c3e50')
        self.root.resizable(False, False)
        
        # Centralizar janela
        self.centralizar_janela()
        
        # Dados
        self.usuarios = {}
        self.produtos = []
        self.usuario_logado = None
        
        # Arquivos de dados
        self.arquivo_usuarios = "usuarios.json"
        self.arquivo_produtos = "produtos.json"
        
        # Carregar dados existentes
        self.carregar_dados()
        
        # Criar interface
        self.criar_interface()
        
    def centralizar_janela(self):
        """Centraliza a janela na tela"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def carregar_dados(self):
        """Carrega dados salvos dos arquivos JSON"""
        try:
            if os.path.exists(self.arquivo_usuarios):
                with open(self.arquivo_usuarios, 'r', encoding='utf-8') as f:
                    self.usuarios = json.load(f)
        except:
            self.usuarios = {}
            
        try:
            if os.path.exists(self.arquivo_produtos):
                with open(self.arquivo_produtos, 'r', encoding='utf-8') as f:
                    self.produtos = json.load(f)
        except:
            self.produtos = []
    
    def salvar_dados(self):
        """Salva dados nos arquivos JSON"""
        try:
            with open(self.arquivo_usuarios, 'w', encoding='utf-8') as f:
                json.dump(self.usuarios, f, ensure_ascii=False, indent=2)
            with open(self.arquivo_produtos, 'w', encoding='utf-8') as f:
                json.dump(self.produtos, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar dados: {e}")
    
    def criar_interface(self):
        """Cria a interface principal"""
        # Frame principal
        self.main_frame = tk.Frame(self.root, bg='#34495e', relief='raised', bd=3)
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Título principal
        title_label = tk.Label(
            self.main_frame, 
            text="SISTEMA DE GESTÃO EMPRESARIAL", 
            font=('Arial', 24, 'bold'), 
            bg='#34495e', 
            fg='white'
        )
        title_label.pack(pady=20)
        
        # Container para conteúdo
        self.content_frame = tk.Frame(self.main_frame, bg='#ecf0f1', relief='sunken', bd=3)
        self.content_frame.pack(expand=True, fill='both', padx=30, pady=20)
        
        # Iniciar com tela de login
        self.mostrar_login()
    
    def limpar_content_frame(self):
        """Limpa o frame de conteúdo"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def mostrar_login(self):
        """Mostra a tela de login"""
        self.limpar_content_frame()
        
        # Frame central para login
        login_frame = tk.Frame(self.content_frame, bg='#ecf0f1')
        login_frame.pack(expand=True)
        
        # Título Login
        tk.Label(
            login_frame, 
            text="ACESSO AO SISTEMA", 
            font=('Arial', 18, 'bold'), 
            bg='#ecf0f1',
            fg='#2c3e50'
        ).pack(pady=30)
        
        # Frame para campos
        campos_frame = tk.Frame(login_frame, bg='#ecf0f1')
        campos_frame.pack(pady=20)
        
        # Campo usuário
        tk.Label(
            campos_frame, 
            text="Usuário:", 
            font=('Arial', 14, 'bold'), 
            bg='#ecf0f1',
            fg='#2c3e50'
        ).grid(row=0, column=0, sticky='e', padx=10, pady=15)
        
        self.entry_login_user = tk.Entry(
            campos_frame, 
            font=('Arial', 14), 
            width=25, 
            relief='solid', 
            bd=2
        )
        self.entry_login_user.grid(row=0, column=1, padx=10, pady=15)
        
        # Campo senha
        tk.Label(
            campos_frame, 
            text="Senha:", 
            font=('Arial', 14, 'bold'), 
            bg='#ecf0f1',
            fg='#2c3e50'
        ).grid(row=1, column=0, sticky='e', padx=10, pady=15)
        
        self.entry_login_pass = tk.Entry(
            campos_frame, 
            font=('Arial', 14), 
            width=25, 
            show="*", 
            relief='solid', 
            bd=2
        )
        self.entry_login_pass.grid(row=1, column=1, padx=10, pady=15)
        
        # Frame para botões
        btn_frame = tk.Frame(login_frame, bg='#ecf0f1')
        btn_frame.pack(pady=30)
        
        # Botão Entrar
        btn_entrar = tk.Button(
            btn_frame, 
            text="ENTRAR", 
            font=('Arial', 14, 'bold'),
            bg='#27ae60', 
            fg='white', 
            width=15, 
            height=2,
            relief='raised',
            bd=3,
            command=self.fazer_login
        )
        btn_entrar.pack(side='left', padx=15)
        
        # Botão Cadastrar Usuário
        btn_cadastrar = tk.Button(
            btn_frame, 
            text="CADASTRAR USUÁRIO", 
            font=('Arial', 14, 'bold'),
            bg='#3498db', 
            fg='white', 
            width=20, 
            height=2,
            relief='raised',
            bd=3,
            command=self.mostrar_cadastro_usuario
        )
        btn_cadastrar.pack(side='left', padx=15)
        
        # Bind Enter key
        self.entry_login_pass.bind('<Return>', lambda e: self.fazer_login())
        
        # Focar no campo usuário
        self.entry_login_user.focus()
    
    def mostrar_cadastro_usuario(self):
        """Mostra a tela de cadastro de usuário"""
        self.limpar_content_frame()
        
        # Frame central
        cadastro_frame = tk.Frame(self.content_frame, bg='#ecf0f1')
        cadastro_frame.pack(expand=True)
        
        # Título
        tk.Label(
            cadastro_frame, 
            text="CADASTRO DE USUÁRIO", 
            font=('Arial', 18, 'bold'), 
            bg='#ecf0f1',
            fg='#2c3e50'
        ).pack(pady=30)
        
        # Frame para campos
        campos_frame = tk.Frame(cadastro_frame, bg='#ecf0f1')
        campos_frame.pack(pady=20)
        
        # Campo nome
        tk.Label(
            campos_frame, 
            text="Nome:", 
            font=('Arial', 14, 'bold'), 
            bg='#ecf0f1',
            fg='#2c3e50'
        ).grid(row=0, column=0, sticky='e', padx=10, pady=15)
        
        self.entry_cad_nome = tk.Entry(
            campos_frame, 
            font=('Arial', 14), 
            width=25, 
            relief='solid', 
            bd=2
        )
        self.entry_cad_nome.grid(row=0, column=1, padx=10, pady=15)
        
        # Campo senha
        tk.Label(
            campos_frame, 
            text="Senha:", 
            font=('Arial', 14, 'bold'), 
            bg='#ecf0f1',
            fg='#2c3e50'
        ).grid(row=1, column=0, sticky='e', padx=10, pady=15)
        
        self.entry_cad_senha = tk.Entry(
            campos_frame, 
            font=('Arial', 14), 
            width=25, 
            show="*", 
            relief='solid', 
            bd=2
        )
        self.entry_cad_senha.grid(row=1, column=1, padx=10, pady=15)
        
        # Frame para botões
        btn_frame = tk.Frame(cadastro_frame, bg='#ecf0f1')
        btn_frame.pack(pady=30)
        
        # Botão Cadastrar
        btn_cadastrar = tk.Button(
            btn_frame, 
            text="CADASTRAR", 
            font=('Arial', 14, 'bold'),
            bg='#e74c3c', 
            fg='white', 
            width=15, 
            height=2,
            relief='raised',
            bd=3,
            command=self.cadastrar_usuario
        )
        btn_cadastrar.pack(side='left', padx=15)
        
        # Botão Voltar
        btn_voltar = tk.Button(
            btn_frame, 
            text="VOLTAR", 
            font=('Arial', 14, 'bold'),
            bg='#95a5a6', 
            fg='white', 
            width=15, 
            height=2,
            relief='raised',
            bd=3,
            command=self.mostrar_login
        )
        btn_voltar.pack(side='left', padx=15)
        
        # Bind Enter key
        self.entry_cad_senha.bind('<Return>', lambda e: self.cadastrar_usuario())
        
        # Focar no campo nome
        self.entry_cad_nome.focus()
    
    def mostrar_produtos(self):
        """Mostra a tela de cadastro de produtos"""
        self.limpar_content_frame()
        
        # Frame principal
        produtos_frame = tk.Frame(self.content_frame, bg='#ecf0f1')
        produtos_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        # Header com título e usuário logado
        header_frame = tk.Frame(produtos_frame, bg='#ecf0f1')
        header_frame.pack(fill='x', pady=(0, 20))
        
        tk.Label(
            header_frame, 
            text="CADASTRO DE PRODUTOS", 
            font=('Arial', 18, 'bold'), 
            bg='#ecf0f1',
            fg='#2c3e50'
        ).pack(side='left')
        
        tk.Label(
            header_frame, 
            text=f"Usuário: {self.usuario_logado}", 
            font=('Arial', 12, 'bold'), 
            bg='#ecf0f1',
            fg='#27ae60'
        ).pack(side='right')
        
        # Frame para campos de entrada
        entrada_frame = tk.LabelFrame(
            produtos_frame, 
            text="Dados do Produto", 
            font=('Arial', 12, 'bold'),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='solid',
            bd=2
        )
        entrada_frame.pack(fill='x', pady=(0, 20))
        
        # Campos do produto
        campos_frame = tk.Frame(entrada_frame, bg='#ecf0f1')
        campos_frame.pack(padx=20, pady=15)
        
        # Campo produto
        tk.Label(
            campos_frame, 
            text="Produto:", 
            font=('Arial', 12, 'bold'), 
            bg='#ecf0f1'
        ).grid(row=0, column=0, sticky='w', padx=5, pady=8)
        
        self.entry_produto = tk.Entry(
            campos_frame, 
            font=('Arial', 12), 
            width=40, 
            relief='solid', 
            bd=2
        )
        self.entry_produto.grid(row=0, column=1, padx=10, pady=8)
        
        # Campo quantidade
        tk.Label(
            campos_frame, 
            text="Quantidade:", 
            font=('Arial', 12, 'bold'), 
            bg='#ecf0f1'
        ).grid(row=1, column=0, sticky='w', padx=5, pady=8)
        
        self.entry_quantidade = tk.Entry(
            campos_frame, 
            font=('Arial', 12), 
            width=40, 
            relief='solid', 
            bd=2
        )
        self.entry_quantidade.grid(row=1, column=1, padx=10, pady=8)
        
        # Campo preço
        tk.Label(
            campos_frame, 
            text="Preço (R$):", 
            font=('Arial', 12, 'bold'), 
            bg='#ecf0f1'
        ).grid(row=2, column=0, sticky='w', padx=5, pady=8)
        
        self.entry_preco = tk.Entry(
            campos_frame, 
            font=('Arial', 12), 
            width=40, 
            relief='solid', 
            bd=2
        )
        self.entry_preco.grid(row=2, column=1, padx=10, pady=8)
        
        # Botões
        btn_frame = tk.Frame(entrada_frame, bg='#ecf0f1')
        btn_frame.pack(pady=15)
        
        tk.Button(
            btn_frame, 
            text="REGISTRAR PRODUTO", 
            font=('Arial', 12, 'bold'),
            bg='#f39c12', 
            fg='white', 
            width=20, 
            height=2,
            relief='raised',
            bd=3,
            command=self.registrar_produto
        ).pack(side='left', padx=10)
        
        tk.Button(
            btn_frame, 
            text="LOGOUT", 
            font=('Arial', 12, 'bold'),
            bg='#e74c3c', 
            fg='white', 
            width=15, 
            height=2,
            relief='raised',
            bd=3,
            command=self.logout
        ).pack(side='left', padx=10)
        
        # Frame para lista de produtos
        lista_frame = tk.LabelFrame(
            produtos_frame, 
            text="Produtos Cadastrados", 
            font=('Arial', 12, 'bold'),
            bg='#ecf0f1',
            fg='#2c3e50',
            relief='solid',
            bd=2
        )
        lista_frame.pack(fill='both', expand=True)
        
        # Treeview para produtos
        columns = ('Produto', 'Quantidade', 'Preço', 'Data')
        self.tree_produtos = ttk.Treeview(lista_frame, columns=columns, show='headings', height=10)
        
        # Configurar colunas
        self.tree_produtos.heading('Produto', text='Produto')
        self.tree_produtos.heading('Quantidade', text='Quantidade')
        self.tree_produtos.heading('Preço', text='Preço (R$)')
        self.tree_produtos.heading('Data', text='Data/Hora')
        
        self.tree_produtos.column('Produto', width=300)
        self.tree_produtos.column('Quantidade', width=100)
        self.tree_produtos.column('Preço', width=100)
        self.tree_produtos.column('Data', width=150)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(lista_frame, orient='vertical', command=self.tree_produtos.yview)
        self.tree_produtos.configure(yscrollcommand=scrollbar.set)
        
        # Pack treeview e scrollbar
        self.tree_produtos.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        scrollbar.pack(side='right', fill='y', pady=10)
        
        # Atualizar lista
        self.atualizar_lista_produtos()
        
        # Bind Enter key
        self.entry_preco.bind('<Return>', lambda e: self.registrar_produto())
        
        # Focar no campo produto
        self.entry_produto.focus()
    
    def cadastrar_usuario(self):
        """Cadastra um novo usuário"""
        nome = self.entry_cad_nome.get().strip()
        senha = self.entry_cad_senha.get().strip()
        
        if not nome or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        if len(nome) < 3:
            messagebox.showerror("Erro", "Nome deve ter pelo menos 3 caracteres!")
            return
            
        if len(senha) < 3:
            messagebox.showerror("Erro", "Senha deve ter pelo menos 3 caracteres!")
            return
        
        if nome in self.usuarios:
            messagebox.showerror("Erro", "Usuário já existe!")
            return
        
        self.usuarios[nome] = senha
        self.salvar_dados()
        
        messagebox.showinfo("Sucesso", f"Usuário '{nome}' cadastrado com sucesso!")
        self.mostrar_login()
    
    def fazer_login(self):
        """Realiza o login do usuário"""
        nome = self.entry_login_user.get().strip()
        senha = self.entry_login_pass.get().strip()
        
        if not nome or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        if nome not in self.usuarios or self.usuarios[nome] != senha:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")
            return
        
        self.usuario_logado = nome
        messagebox.showinfo("Sucesso", f"Bem-vindo, {nome}!")
        self.mostrar_produtos()
    
    def registrar_produto(self):
        """Registra um novo produto"""
        if not self.usuario_logado:
            messagebox.showerror("Erro", "Faça login primeiro!")
            return
        
        nome = self.entry_produto.get().strip()
        quantidade = self.entry_quantidade.get().strip()
        preco = self.entry_preco.get().strip()
        
        if not nome or not quantidade or not preco:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        try:
            quantidade_int = int(quantidade)
            if quantidade_int <= 0:
                raise ValueError("Quantidade deve ser positiva")
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser um número inteiro positivo!")
            return
        
        try:
            preco_float = float(preco.replace(',', '.'))
            if preco_float <= 0:
                raise ValueError("Preço deve ser positivo")
        except ValueError:
            messagebox.showerror("Erro", "Preço deve ser um número positivo!")
            return
        
        produto = {
            'nome': nome,
            'quantidade': quantidade_int,
            'preco': preco_float,
            'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'usuario': self.usuario_logado
        }
        
        self.produtos.append(produto)
        self.salvar_dados()
        
        messagebox.showinfo("Sucesso", f"Produto '{nome}' registrado com sucesso!")
        
        # Limpar campos
        self.entry_produto.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        
        # Atualizar lista
        self.atualizar_lista_produtos()
        
        # Focar no campo produto
        self.entry_produto.focus()
    
    def atualizar_lista_produtos(self):
        """Atualiza a lista de produtos na treeview"""
        # Limpar itens existentes
        for item in self.tree_produtos.get_children():
            self.tree_produtos.delete(item)
        
        # Adicionar produtos
        for produto in reversed(self.produtos):  # Mais recentes primeiro
            self.tree_produtos.insert('', 'end', values=(
                produto['nome'],
                produto['quantidade'],
                f"R$ {produto['preco']:.2f}",
                produto['data']
            ))
    
    def logout(self):
        """Faz logout do usuário"""
        self.usuario_logado = None
        messagebox.showinfo("Logout", "Logout realizado com sucesso!")
        self.mostrar_login()
    
    def executar(self):
        """Executa a aplicação"""
        self.root.mainloop()

if __name__ == "__main__":
    app = SistemaCompleto()
    app.executar()