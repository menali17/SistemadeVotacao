
from package.pessoa import Pessoa

class Eleitor(Pessoa):
    def __init__(self, nome, cpf, rg, data_nascimento, cep):
        super().__init__(nome, cpf, rg, data_nascimento, cep)

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "rg": self.rg,
            "data_nascimento": self.data_nascimento,
            "cep": self.cep
        }


