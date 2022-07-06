
class Interesse:
    
    def __init__(self, Marca : str, Modelo : str, Fonte : str, ID_User = -1):
        self.__marca = Marca
        self.__modelo = Modelo
        self.__fonte = Fonte
        self.__user_id = ID_User
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getFonte(self):
        return self.__fonte
    
    def getUserID(self):
        return self.__user_id