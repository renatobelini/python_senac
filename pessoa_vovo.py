from pessoa import Pessoa

class Vovo(Pessoa):

    nome =""

    def __init__(self, nome = None,  mae = None):
        super().__init__(nome, mae)

    def andar(self):
        print("ja sou bem grandinha, sei andar sozinha")

    def idade(self, idade):
        self.idade = idade
        print("eu tenho ", idade, " anos.")
