import mysql.connector

class ParticipantesDAO:
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def insertCarros(self, listaCarros : Carro) -> bool: