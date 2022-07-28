
from BaseDados.CarrosDAO import CarrosDAO


class CarrosFacade:

    def __init__(self):
        pass

    def getImagensCarros(self) -> list:
        carrosDAO = CarrosDAO.instance()
        return carrosDAO.getImagensCarros()

    def getTodosCarrosPorInteresse(self, id_user : int, marca : str, modelo : str) -> list:
        carrosDAO = CarrosDAO.instance()

        if (marca == '' and modelo == ''):
            temp = carrosDAO.getAllCarrosInteresseByUtilizador(id_user)
        else:
            temp = carrosDAO.getAllCarrosByMarcaANDModelo(marca, modelo, id_user)
        
        res = []
        for carro in temp:
            carroSerializable = carro.serialize()
            res.append(carroSerializable)
        
        return res

    def getTodosCarrosNaoVistos(self, id_user : int) -> list:
        carrosDAO = CarrosDAO.instance()

        carros_nao_vistos = carrosDAO.getAllCarrosNaoVistos(id_user)
        carrosDAO.marcaCarrosComoVistos(id_user)
        
        res = []
        for carro in carros_nao_vistos:
            carroSerializable = carro.serialize()
            res.append(carroSerializable)
        
        return res

    def getTodosCarrosFavoritos(self, id_user : int) -> list:
        carrosDAO = CarrosDAO.instance()

        temp = carrosDAO.getAllCarrosFavoritos(id_user)
        res = []
        for carro in temp:
            carroSerializable = carro.serialize()
            res.append(carroSerializable)
        
        return res

    def getTodosCarrosAvailable(self, id_user : int, marca : list, modelo : str, filtro, num_pagina : int, ordem : str) -> list:
        carrosDAO = CarrosDAO.instance()

        temp = carrosDAO.getAllCarrosAvailable(id_user, marca, modelo, filtro, num_pagina, ordem)
        res = []
        for carro in temp:
            carroSerializable = carro.serialize()
            res.append(carroSerializable)
        pages = carrosDAO.getNumPagesCarrosAvailable(marca, modelo, filtro, num_pagina)
        
        return res, pages