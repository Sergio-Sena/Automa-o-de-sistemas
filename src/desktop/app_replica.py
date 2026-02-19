import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class AppReplica:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Cadastro - Replica")
        self.root.geometry("400x500")
        self.root.configure(bg='#f0f0f0')
        
        # Dados
        self.usuarios = {}
        self.produtos = []
        self.usuario_logado = None
        self.arquivo_usuarios = "usuarios.json"
        self.arquivo_produtos = "produtos.json"
        
        # Carregar dados
        self.carregar_dados()
        
        # Criar interface
        self.criar_interface()
        
    def carregar_dados(self):
        """Carrega dados salvos"""
        if os.path.exists(self.arquivo_usuarios):
            try:
                with open(self.arquivo_usuarios, 'r') as f:
                    self.usuarios = json.load(f)
            except:
                self.usuarios = {}
                
        if os.path.exists(self.arquivo_produtos):
            try:
                with open(self.arquivo_produtos, 'r') as f:
                    self.produtos = json.load(f)
            except:
                self.produtos = []
    
    def salvar_dados(self):
        """Salva dados"""
        with open(self.arquivo_usuarios, 'w') as f:
            json.dump(self.usuarios, f)
        with open(self.arquivo_produtos, 'w') as f:
            json.dump(self.produtos, f)
    
    def criar_interface(self):
        """Cria interface principal"""
        # Notebook para abas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Aba Login
        self.frame_login = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_login, text="Login")
        self.criar_aba_login()
        
        # Aba Cadastro Usuário
        self.frame_cadastro_user = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_cadastro_user, text="Cadastrar Usuário")
        self.criar_aba_cadastro_usuario()
        
        # Aba Produtos (inicialmente desabilitada)
        self.frame_produtos = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_produtos, text="Produtos", state='disabled')
        self.criar_aba_produtos()
    
    def criar_aba_login(self):
        """Cria aba de login"""
        ttk.Label(self.frame_login, text="LOGIN", font=('Arial', 16, 'bold')).pack(pady=20)
        
        ttk.Label(self.frame_login, text="Usuário:").pack(pady=5)
        self.entry_login_user = ttk.Entry(self.frame_login, width=30)
        self.entry_login_user.pack(pady=5)
        
        ttk.Label(self.frame_login, text="Senha:").pack(pady=5)
        self.entry_login_pass = ttk.Entry(self.frame_login, width=30, show="*")
        self.entry_login_pass.pack(pady=5)
        
        ttk.Button(self.frame_login, text="Entrar", command=self.fazer_login).pack(pady=20)
    
    def criar_aba_cadastro_usuario(self):
        """Cria aba de cadastro de usuário"""
        ttk.Label(self.frame_cadastro_user, text="CADASTRAR USUÁRIO", font=('Arial', 16, 'bold')).pack(pady=20)
        
        ttk.Label(self.frame_cadastro_user, text="Nome:").pack(pady=5)
        self.entry_cad_nome = ttk.Entry(self.frame_cadastro_user, width=30)
        self.entry_cad_nome.pack(pady=5)
        
        ttk.Label(self.frame_cadastro_user, text="Senha:").pack(pady=5)
        self.entry_cad_senha = ttk.Entry(self.frame_cadastro_user, width=30, show="*")
        self.entry_cad_senha.pack(pady=5)
        
        ttk.Button(self.frame_cadastro_user, text="Cadastrar", command=self.cadastrar_usuario).pack(pady=20)
    
    def criar_aba_produtos(self):
        """Cria aba de produtos"""
        ttk.Label(self.frame_produtos, text="CADASTRO DE PRODUTOS", font=('Arial', 16, 'bold')).pack(pady=10)
        
        ttk.Label(self.frame_produtos, text="Nome do Produto:").pack(pady=2)
        self.entry_produto = ttk.Entry(self.frame_produtos, width=30)
        self.entry_produto.pack(pady=2)
        
        ttk.Label(self.frame_produtos, text="Quantidade:").pack(pady=2)
        self.entry_quantidade = ttk.Entry(self.frame_produtos, width=30)
        self.entry_quantidade.pack(pady=2)
        
        ttk.Label(self.frame_produtos, text="Preço:").pack(pady=2)
        self.entry_preco = ttk.Entry(self.frame_produtos, width=30)
        self.entry_preco.pack(pady=2)
        
        ttk.Button(self.frame_produtos, text="Registrar", command=self.registrar_produto).pack(pady=15)
        
        # Lista de produtos
        self.lista_produtos = tk.Listbox(self.frame_produtos, height=8)
        self.lista_produtos.pack(pady=10, fill='x', padx=10)
        
        self.atualizar_lista_produtos()
    
    def cadastrar_usuario(self):
        """Cadastra novo usuário"""
        nome = self.entry_cad_nome.get().strip()
        senha = self.entry_cad_senha.get().strip()
        
        if not nome or not senha:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        
        if nome in self.usuarios:
            messagebox.showerror("Erro", "Usuário já existe!")
            return
        
        self.usuarios[nome] = senha
        self.salvar_dados()
        
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        self.entry_cad_nome.delete(0, tk.END)
        self.entry_cad_senha.delete(0, tk.END)
    
    def fazer_login(self):
        """Realiza login"""
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
        
        # Habilitar aba produtos
        self.notebook.tab(2, state='normal')
        self.notebook.select(2)
    
    def registrar_produto(self):
        """Registra novo produto"""
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
            quantidade = int(quantidade)
            preco = float(preco)
        except ValueError:
            messagebox.showerror("Erro", "Quantidade e preço devem ser números!")
            return
        
        produto = {
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco,
            'data': datetime.now().strftime('%d/%m/%Y %H:%M')
        }
        
        self.produtos.append(produto)
        self.salvar_dados()
        
        messagebox.showinfo("Sucesso", "Produto registrado!")
        
        # Limpar campos
        self.entry_produto.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        
        self.atualizar_lista_produtos()
    
    def atualizar_lista_produtos(self):
        """Atualiza lista de produtos"""
        self.lista_produtos.delete(0, tk.END)
        for produto in self.produtos:
            texto = f"{produto['nome']} - Qtd: {produto['quantidade']} - R$ {produto['preco']:.2f}"
            self.lista_produtos.insert(tk.END, texto)
    
    def executar(self):
        """Executa a aplicação"""
        self.root.mainloop()

if __name__ == "__main__":
    app = AppReplica()
    app.executar()