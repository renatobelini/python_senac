class Calculos_01(object):
    #calculando o dolar
    def calculoRealDolar(self, real):
        dolar = 3.1410;
        print ("")
        print ("")
        print ("            Real: ", real)
        print ("            Dolar Atual: ", dolar)
        print ("            Dolar Convertido: ", real * dolar)
        print ("")
        print ("")

    #converter em pes a altura de uma pessoa
    def convertPesAltura(self, pes):
        metro = pes / 3.2808
        print ("")
        print ("")
        print ("            Pes: ", pes)        
        print ("            Metros: ", metro)
        print ("")
        print ("")

    # calcular a capacidade maxima de pessosas dentro de uma sala
    def capacidadeSala(self, comprimento, largura):
        # 1 pessoa por metro quadrado
        print ("")
        print ("")
        print ("            1 pessoa por metro quadrado")
        print ("            cabem: ", comprimento *largura, " pessoas")
        print ("")
        print ("")        

opcao =0

while opcao != 4:
    #inicio
    print("""Seja Bem Vindo

            selecione uma opção
            [ 1 ] - calcular real em dolar
            [ 2 ] - converter em pes a altura de uma pessoa
            [ 3 ] - calcular a capacidade maxima de pessosas dentro de uma sala
            [ 4 ] - sair
            
            """)

    opcao = int(input())

    c = Calculos_01()

    
    if opcao == 1:
        real = int(input("            Informe o valor em Real: "))
        c.calculoRealDolar(real)
    elif opcao ==2:
        pes = int(input("            Informe quantos pes: "))
        c.convertPesAltura(pes)
    elif opcao ==3:
        comprimento = int(input("            Informe o comprimento da sala: "))
        largura = int(input("            Informe a largura da sala: "))
        c.capacidadeSala(comprimento, largura)

    
    #fim do while !=4



