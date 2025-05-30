
from datetime import datetime

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if not cpf or len(cpf) != 11 or cpf == cpf[0] * len(cpf):
        return False

    def calcular_digito(cpf_parcial):
        soma = sum(int(digito) * peso for digito, peso in zip(cpf_parcial, range(len(cpf_parcial) + 1, 1, -1)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    primeiro_digito = calcular_digito(cpf[:9])
    segundo_digito = calcular_digito(cpf[:9] + primeiro_digito)

    return cpf.endswith(primeiro_digito + segundo_digito)

def validar_cep(cep):
    return cep.isdigit() and len(cep) == 8

def validar_data(data_nasc):
    try:
        dia, mes, ano = map(int, data_nasc.split('/'))
        data = datetime(ano, mes, dia)
        return data
    except (ValueError, TypeError):
        return None


from datetime import datetime

def calcular_idade(data_nascimento):
    try:
        nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        hoje = datetime.today()
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return idade
    except Exception as e:
        print("Erro ao calcular idade:", e)
        return None
