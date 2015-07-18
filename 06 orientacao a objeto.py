#old-Style
class Pessoa(object):
    nome = ""
    idade = 0

    def __init__(self, nome):
        self.nome = nome   
    
    def andar(self):
        print("a pessoa esta andando ....")
    
p = Pessoa('belini')
#p.nome = 'renato'
p.idade = 20

print("nome: ", p.nome, " / idade: ", p.idade)
p.andar()
