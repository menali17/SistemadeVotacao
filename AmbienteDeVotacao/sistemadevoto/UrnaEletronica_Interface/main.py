from package.urna import UrnaEletronica
from package.interface_urna_exibir_candidato import InterfaceUrna

if __name__ == "__main__":
    urna = UrnaEletronica()
    app = InterfaceUrna(urna)
    app.janela.mainloop()
