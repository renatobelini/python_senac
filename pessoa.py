class Pessoa(object):

    def __init__(self, nome, mae):
        self.nome = nome
        self.mae = mae
        print("metodo construtor da super classe")

    def andar(self):
        print("aprendendo a caminhar")

    def chorar(self):
        print("muleque chorando pq caiu!!")
        
