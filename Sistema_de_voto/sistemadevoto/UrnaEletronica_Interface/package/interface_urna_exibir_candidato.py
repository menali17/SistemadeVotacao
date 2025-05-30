
import tkinter as tk
from tkinter import messagebox
from package.urna import UrnaEletronica
from package.candidato import CANDIDATOS


class InterfaceUrna:
    def __init__(self, urna: UrnaEletronica):
        self.urna = urna
        self.cpf = ""
        self.numero = ""
        self.cargo_atual = 0
        self.cargos = list(CANDIDATOS.keys())
        self.voto = {}

        self.janela = tk.Tk()
        self.janela.title("Urna Eletrônica")
        self.janela.geometry("400x600")
        self.janela.configure(bg="white")

        self.tela_cpf()

    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def tela_cpf(self):
        self.limpar_tela()
        self.numero = ""
        tk.Label(self.janela, text="Digite seu CPF", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

        self.display = tk.Entry(self.janela, font=("Arial", 24), justify="center")
        self.display.pack(pady=10)

        self.teclado(self.processar_cpf, self.limpar_display, self.confirmar_cpf)

    def processar_cpf(self, valor):
        self.numero += valor
        self.display.delete(0, tk.END)
        self.display.insert(0, self.numero)

    def limpar_display(self):
        self.numero = ""
        self.display.delete(0, tk.END)

    def confirmar_cpf(self):
        cpf = self.display.get().strip()
        if not self.urna.cpf_valido(cpf):
            messagebox.showerror("Erro", "CPF inválido.")
            return
        if self.urna.eleitor_ja_votou(cpf):
            messagebox.showerror("Erro", "Este CPF já votou.")
            return
        self.cpf = cpf
        self.tela_voto()

    def tela_voto(self):
        self.limpar_tela()
        self.numero = ""
        if self.cargo_atual >= len(self.cargos):
            self.finalizar_votacao()
            return

        self.cargo = self.cargos[self.cargo_atual]
        self.candidatos = CANDIDATOS[self.cargo]

        tk.Label(self.janela, text=f"Cargo: {self.cargo}", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

        self.display = tk.Entry(self.janela, font=("Arial", 24), justify="center")
        self.display.pack(pady=10)

        self.resultado_label = tk.Label(self.janela, text="", font=("Arial", 14), bg="white")
        self.resultado_label.pack(pady=5)

        self.teclado(self.processar_voto, self.limpar_display, self.confirmar_voto, incluir_branco=True)

    def processar_voto(self, valor):
        self.numero += valor
        self.display.delete(0, tk.END)
        self.display.insert(0, self.numero)

        candidato = self.candidatos.get(self.numero, None)
        if candidato:
            self.resultado_label.config(text=f"Candidato: {candidato}")
        else:
            self.resultado_label.config(text="VOTO NULO")

    def confirmar_voto(self):
        numero = self.display.get().strip()
        candidato = self.candidatos.get(numero, None)
        if numero.lower() == "branco":
            self.voto[self.cargo] = "BRANCO"
        elif candidato:
            self.voto[self.cargo] = candidato
        else:
            self.voto[self.cargo] = "VOTO NULO"

        self.cargo_atual += 1
        self.tela_voto()

    def voto_branco(self):
        self.voto[self.cargo] = "BRANCO"
        self.cargo_atual += 1
        self.tela_voto()

    def finalizar_votacao(self):
        self.urna.registrar_voto(self.cpf, self.voto)
        messagebox.showinfo("FIM", "Votação concluída com sucesso!")
        self.janela.destroy()

    def teclado(self, func_num, func_corrige, func_confirma, incluir_branco=False):
        frame = tk.Frame(self.janela, bg="white")
        frame.pack()

        botoes = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

        for linha in botoes:
            linha_frame = tk.Frame(frame, bg="white")
            linha_frame.pack(pady=2)
            for botao in linha:
                tk.Button(
                    linha_frame, text=botao, width=5, height=2, bg="gray", fg="white",
                    command=lambda b=botao: func_num(b)
                ).pack(side="left", padx=5)

        linha_final = tk.Frame(frame, bg="white")
        linha_final.pack(pady=5)

        if incluir_branco:
            tk.Button(
                linha_final, text="BRANCO", width=5, height=2, bg="gray", fg="white",
                command=self.voto_branco
            ).pack(side="left", padx=5)
        else:
            tk.Label(linha_final, text=" ", bg="white", width=5).pack(side="left", padx=5)

        tk.Button(
            linha_final, text="0", width=5, height=2, bg="gray", fg="white",
            command=lambda: func_num("0")
        ).pack(side="left", padx=5)

        tk.Button(
            linha_final, text="CORRIGE", width=7, height=2, bg="orange", fg="white",
            command=func_corrige
        ).pack(side="left", padx=5)

        tk.Button(
            self.janela, text="CONFIRMA", width=20, height=2, bg="green", fg="white",
            command=func_confirma
        ).pack(pady=10)
