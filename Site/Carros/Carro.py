
class Carro:
    
    def __init__(self, ID : int, Anunciante : str, Marca : str, Modelo : str, Versao : str, Combustivel : str, Mes_Registo : str, Ano : int, 
                Quilometros : int, Cilindrada : int, Potencia : int, Cor : str, Tipo_Cor : str, Tipo_Caixa : str, Num_Portas : int, 
                Origem : str, Condicao : str, Preco : float, Link_foto = '', Titulo = '', Link_anuncio = ''
    ):
        self.__id = ID
        self.__anunciante = Anunciante
        self.__marca = Marca
        self.__modelo = Modelo
        self.__versao = Versao
        self.__combustivel = Combustivel
        self.__mes_registo = Mes_Registo
        self.__ano = Ano
        self.__quilometros = Quilometros
        self.__cilindrada = Cilindrada
        self.__potencia = Potencia
        self.__cor = Cor
        self.__tipo_cor = Tipo_Cor
        self.__tipo_caixa = Tipo_Caixa
        self.__num_portas = Num_Portas
        self.__origem = Origem
        self.__condicao = Condicao
        self.__preco = Preco
        self.__link_foto = Link_foto
        self.__titulo = Titulo
        self.__link_anuncio = Link_anuncio
    
    def getID(self):
        return self.__id

    def getAnunciante(self):
        return self.__anunciante
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getVersao(self):
        return self.__versao
    
    def getCombustivel(self):
        return self.__combustivel
    
    def getMes_Registo(self):
        return self.__mes_registo
    
    def getAno(self):
        return self.__ano
    
    def getQuilometros(self):
        return self.__quilometros
    
    def getCilindrada(self):
        return self.__cilindrada
    
    def getPotencia(self):
        return self.__potencia
    
    def getCor(self):
        return self.__cor
    
    def getTipo_Cor(self):
        return self.__tipo_cor
    
    def getTipo_Caixa(self):
        return self.__tipo_caixa
    
    def getNum_Portas(self):
        return self.__num_portas

    def getOrigem(self):
        return self.__origem

    def getCondicao(self):
        return self.__condicao

    def getPreco(self):
        return self.__preco
    
    def getLink_foto(self):
        return self.__link_foto
    
    def getTitulo(self):
        return self.__titulo
    
    def getLink_anuncio(self):
        return self.__link_anuncio