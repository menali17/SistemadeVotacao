
import os
import json
from package.eleitor import Eleitor

class CadastroEleitor:
    def __init__(self, arquivo="dados/eleitores.json"):
        self.arquivo = arquivo
        self.eleitores = {}
        os.makedirs("dados", exist_ok=True)
        self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.eleitores = {cpf: Eleitor(**info) for cpf, info in dados.items()}
        else:
            self.eleitores = {}

    def salvar_dados(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump({cpf: eleitor.to_dict() for cpf, eleitor in self.eleitores.items()}, f, ensure_ascii=False, indent=4)

    def cpf_existe(self, cpf):
        return cpf in self.eleitores

    def adicionar_eleitor(self, eleitor: Eleitor):
        self.eleitores[eleitor.cpf] = eleitor
        self.salvar_dados()
