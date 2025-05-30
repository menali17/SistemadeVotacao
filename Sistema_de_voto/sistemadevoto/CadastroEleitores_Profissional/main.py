
from package.cadastro import CadastroEleitor
from package.interface import InterfaceCadastro

if __name__ == "__main__":
    cadastro = CadastroEleitor()
    app = InterfaceCadastro(cadastro)
    app.iniciar()
