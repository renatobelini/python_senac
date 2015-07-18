class converte_dolar(object):
    #calculando o dolar
    def converter_dolar(self, real):
        dolarAtual = 3.1410
        print ("")
        print ("")
        print ("            Real: ", real)
        print ("            Dolar Atual: ", dolarAtual)
        print ("            Dolar Convertido: ", real * dolarAtual)
        print ("")
        print ("")


    #converter em pes a altura de uma pessoa
    def converterPesEmAltura(self, pes):
        metro = pes / 3.2808

        def __init__(self, pes):
            self.pes = pes
        
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


# ----------------------------   executando ---------------------------
real = int(input("            Informe o valor em Real: "))
c = converte_dolar()
c.converter_dolar(real)

# -------------------------------------------------------------------------------
pes = int(input("            Informe quantos pes: "))
p = converterPesEmAltura(pes)

# -------------------------------------------------------------------------------
comprimento = int(input("            Informe o comprimento da sala: "))
largura = int(input("            Informe a largura da sala: "))

capacidade = capacidadeSala(comprimento, largura)
 
        
