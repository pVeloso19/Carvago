class User:

    def __init__(self, idUser: int, nome: str, email: str, password: str):
        self.__idUser = idUser
        self.__nome = nome
        self.__email = email
        self.__password = password

    def getIdUser(self) -> int:
        return self.__idUser

    def setIdUser(self, idUser: int):
        self.__idUser = idUser

    def getNome(self) -> str:
        return self.__nome

    def setNome(self, nome: str):
        self.__nome = nome

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, email: str):
        self.__email = email

    def getPassword(self) -> str:
        return self.__password

    def setPassword(self, password: str):
        self.__password = password
