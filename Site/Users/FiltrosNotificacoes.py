
class FiltrosNotificacoes:
    
    def __init__(self, idFiltros : int, AnoMinimo : int, AnoMaximo : int, PrecoMinimo : float, PrecoMaximo : float, Combustivel : str, 
                 KM_Minimo : int, KM_Maximo : int):
        self.__id_filtros = idFiltros
        self.__ano_minimo = AnoMinimo
        self.__ano_maximo = AnoMaximo
        self.__preco_minimo = PrecoMinimo
        self.__preco_maximo = PrecoMaximo
        self.__combustivel = Combustivel
        self.__KM_minimo = KM_Minimo
        self.__KM_maximo = KM_Maximo

    def getIDFiltros(self):
        return self.__id_filtros
    
    def getAnoMinimo(self):
        return self.__ano_minimo

    def getAnoMaximo(self):
        return self.__ano_maximo

    def getPrecoMinimo(self):
        return self.__preco_minimo

    def getPrecoMaximo(self):
        return self.__preco_maximo

    def getCombustivel(self):
        return self.__combustivel

    def getKMMinimo(self):
        return self.__KM_minimo

    def getKMMaximo(self):
        return self.__KM_maximo