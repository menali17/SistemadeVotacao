
from datetime import datetime

class Eleitor:
    def __init__(self, nome, cpf, rg, cep, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.cep = cep
        self.data_nascimento = data_nascimento

    def calcular_idade(self):
        nascimento = datetime.strptime(self.data_nascimento, "%d/%m/%Y")
        hoje = datetime.today()
        return hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "rg": self.rg,
            "cep": self.cep,
            "data_nascimento": self.data_nascimento
        }
