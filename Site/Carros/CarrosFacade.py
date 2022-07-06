
from BaseDados.CarrosDAO import CarrosDAO


class CarrosFacade:

    def __init__(self):
        pass

    def getTodosCarrosPorInteresse(self, id_user : int, marca : str, modelo : str) -> list:
        carrosDAO = CarrosDAO.instance()

        temp = carrosDAO.getAllCarrosByMarcaANDModelo(marca, modelo)
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
