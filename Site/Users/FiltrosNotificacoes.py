
class FiltrosNotificacoes:
    
    def __init__(self, idFiltros : int, AnoMinimo : int, AnoMaximo : int, PrecoMinimo : float, PrecoMaximo : float, Combustivel : str, 
                 KM_Minimo : int, KM_Maximo : int):
        self.__id_filtros = idFiltros
        self.__ano_minimo = 0 if (AnoMinimo == '' or AnoMinimo == 'NULL') else int(AnoMinimo)
        self.__ano_maximo = 5030 if (AnoMaximo == '' or AnoMaximo == 'NULL') else int(AnoMaximo)
        self.__preco_minimo = -1 if (PrecoMinimo == '' or PrecoMinimo == 'NULL') else float(PrecoMinimo)
        self.__preco_maximo = 99999999 if (PrecoMaximo == '' or PrecoMaximo == 'NULL') else float(PrecoMaximo)
        self.__combustivel = Combustivel
        self.__KM_minimo = -1 if (KM_Minimo == '' or KM_Minimo == 'NULL') else int(KM_Minimo)
        self.__KM_maximo = 99999999 if (KM_Maximo == '' or KM_Maximo == 'NULL') else int(KM_Maximo)

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