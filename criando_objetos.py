from pessoa import Pessoa
from pessoa_bb import BB
from pessoa_vovo import Vovo
#instanciando um objeto do tipo BB
bb1 = BB("joao gabriel","thaline andre")
#imprime o BB criado ..
print("nome: " +bb1.nome)
print("nome: " +bb1.mae)
#metodo definido na super classe Pessoa
bb1.andar()
#metodo definido na sub-classe BB
bb1.bicicleta()
#metodo chrar da super classe
bb1.chorar()
print("-----------------------------------------------------------")
#instanciando um objeto do tipo pessoa
p1 = Pessoa("joao miguel", "emanuela carvalho")
#imprime a pessoa criada ..
print("nome: " +p1.nome)
print("nome: " +p1.mae)
#metodo definido na propria classe
p1.andar()
p1.chorar()

vovo1 = Vovo()
vovo1.andar()
vovo1.idade(80)

#isso vai dar merda federal!! :(
#p1.bicicleta()#este metodo esta definido na subclasse, por isso nao funciona
