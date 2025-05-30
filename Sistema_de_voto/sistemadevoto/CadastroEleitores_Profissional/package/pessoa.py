
class Pessoa:
    def __init__(self, nome, cpf, rg, data_nascimento, cep):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento
        self.cep = cep

    def exibir_dados(self):
        return f"Nome: {self.nome} | CPF: {self.cpf}"
