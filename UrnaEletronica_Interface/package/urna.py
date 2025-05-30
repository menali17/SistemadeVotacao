
import os
import json
from package.candidato import CANDIDATOS

class UrnaEletronica:
    def __init__(self, arquivo_eleitores="../CadastroEleitores_Profissional/dados/eleitores.json", arquivo_votos="dados/votos/todos_os_votos.json"):
        self.arquivo_eleitores = arquivo_eleitores
        self.arquivo_votos = arquivo_votos
        self.eleitores = {}
        os.makedirs("dados/votos", exist_ok=True)
        self.carregar_eleitores()

    def carregar_eleitores(self):
        if os.path.exists(self.arquivo_eleitores):
            with open(self.arquivo_eleitores, "r", encoding="utf-8") as f:
                self.eleitores = json.load(f)
        else:
            self.eleitores = {}
            print("Arquivo de eleitores não encontrado. Nenhum eleitor cadastrado.")

    def cpf_valido(self, cpf):
        return cpf in self.eleitores

    def eleitor_ja_votou(self, cpf):
        if not os.path.exists(self.arquivo_votos):
            return False
        with open(self.arquivo_votos, "r", encoding="utf-8") as f:
            todos_votos = json.load(f)
        return cpf in todos_votos

    def registrar_voto(self, cpf, votos):
        if os.path.exists(self.arquivo_votos):
            with open(self.arquivo_votos, "r", encoding="utf-8") as f:
                todos_votos = json.load(f)
        else:
            todos_votos = {}

        todos_votos[cpf] = votos

        with open(self.arquivo_votos, "w", encoding="utf-8") as f:
            json.dump(todos_votos, f, ensure_ascii=False, indent=4)
