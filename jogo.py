from random import randint
print("Bem Vindo!!!")
#print(numero_sorteado)
novo_jogo = True
while novo_jogo != False:
    contador = 1
    numero_sorteado = randint(1,5)
    while True:
        chute = int(input("chute um numero: "))
        if chute == numero_sorteado:
            print("paarabens, voce é foda.")
            break
        else:
            print("chute um numero Baixo" if chute > numero_sorteado else "chute um numero Alto")
        contador +=1
    print("Fim de Jogo")
    print("Numero sorteado: " + str(numero_sorteado))
    print("Numero chutado: " + str(chute))
    print("numero de tentativas: " + str(contador))
    novo_jogo = int(input("jogar novamente? 1 - Sim 0 - Não: "))
