
from datetime import datetime

class Validador:
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        return cpf.isdigit() and len(cpf) == 11

    @staticmethod
    def validar_cep(cep: str) -> bool:
        return cep.isdigit() and len(cep) == 8

    @staticmethod
    def validar_data_nascimento(data_nascimento: str) -> bool:
        try:
            datetime.strptime(data_nascimento, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    @staticmethod
    def calcular_idade(data_nascimento: str) -> int:
        try:
            nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
            hoje = datetime.today()
            idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
            return idade
        except ValueError:
            return None
