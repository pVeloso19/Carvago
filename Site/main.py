from API.StandVirtualFont import StandVirtualGather
from BaseDados.CarrosDAO import CarrosDAO

stand_virtual = StandVirtualGather()
dados = stand_virtual.getDados()

print('dados ok')

carrosDAO = CarrosDAO.instance()
carrosDAO.insertCarros(dados)
