
import tkinter as tk
from tkinter import messagebox
from package.eleitor import Eleitor
from package.validacoes import Validador
from package.cadastro import CadastroEleitor
from package.validacoes import Validador

class InterfaceCadastro:
    def __init__(self, cadastro: CadastroEleitor):
        self.cadastro = cadastro
        self.janela = tk.Tk()
        self.janela.title("Cadastro de Eleitores - Sistema Brasileiro")
        self.janela.geometry("600x600")
        self.janela.configure(bg="white")
        self.criar_interface()

    def criar_interface(self):
        tk.Label(self.janela, text="Cadastro de Eleitores", bg="green", fg="white", font=("Arial", 22, "bold")).pack(fill=tk.X, pady=10)
        tk.Label(self.janela, text="🇧🇷 Sistema Brasileiro 🇧🇷", bg="yellow", fg="blue", font=("Arial", 18, "bold")).pack(fill=tk.X, pady=5)

        frame = tk.Frame(self.janela, bg="white")
        frame.pack(pady=20)

        labels = ["Nome Completo:", "CPF (11 dígitos):", "RG:", "CEP (8 dígitos):", "Data de Nascimento (dd/mm/aaaa):"]
        self.entries = []

        for i, label in enumerate(labels):
            tk.Label(frame, text=label, bg="white", anchor="w", font=("Arial", 12)).grid(row=i, column=0, sticky="w", pady=5, padx=5)
            entry = tk.Entry(frame, width=40, font=("Arial", 12))
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries.append(entry)

        tk.Button(self.janela, text="Cadastrar Eleitor", bg="green", fg="white", width=25, height=2, font=("Arial", 12), command=self.cadastrar_eleitor).pack(pady=20)

        

    def cadastrar_eleitor(self):
        dados = [entry.get().strip() for entry in self.entries]
        if not all(dados):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        nome, cpf, rg, cep, data_nasc = dados

        if not Validador.validar_cpf(cpf):
            messagebox.showerror("Erro", "CPF inválido.")
            return

        if not Validador.validar_cep(cep):
            messagebox.showerror("Erro", "CEP inválido. Deve conter 8 dígitos.")
            return

        data = Validador.validar_data_nascimento(data_nasc)
        if not data:
            messagebox.showerror("Erro", "Data de nascimento inválida. Use o formato dd/mm/aaaa.")
            return

        idade = Validador.calcular_idade(data_nasc)
        if idade is None:
            messagebox.showerror("Erro", "Data de nascimento inválida. Use o formato DD/MM/AAAA.")
            return
        if idade < 16:
            messagebox.showerror("Erro", "Idade mínima para cadastro é 16 anos.")
            return

        if self.cadastro.cpf_existe(cpf):
            messagebox.showerror("Erro", "CPF já cadastrado.")
            return

        eleitor = Eleitor(nome, cpf, rg, cep, data_nasc)
        self.cadastro.adicionar_eleitor(eleitor)
        messagebox.showinfo("Sucesso", "Eleitor cadastrado com sucesso!")
        self.limpar_campos()

    def limpar_campos(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

    def iniciar(self):
        self.janela.mainloop()