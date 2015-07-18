#realiza a importacao da classe pessoa
from pessoa import Pessoa

class BB(Pessoa):
    def __init__(self, nome, mae):
        print("metodo construtor da sub-classe")
        super().__init__(nome,mae)
        self.nome = nome
        self.mae = mae

    def bicicleta(self):
        print("agora aprendendo a pedalar ...")
