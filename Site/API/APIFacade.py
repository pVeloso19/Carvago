from API.StandVirtualFont import StandVirtualGather
from API.OlxFont import OLXGather
from Users.UserFacade import UserFacade


class APIFacade:
    def __init__(self):
        pass

    def getDados(self):
        #Inicia todas as fontes
        stand_virtual = StandVirtualGather()
        olx = OLXGather()

        #Obtem todos os interesses para cada fonte
        userFacade = UserFacade()
        fontes = userFacade.getInteressesUser()

        # Obtem os carros
        carros_novos = []
        id_carros_vendidos = []
        for fonte, interesses in fontes.items():
            if(fonte == 'stand-virtual'):
                novos, vendidos = stand_virtual.getDados(interesses)
                carros_novos.extend(novos)
                id_carros_vendidos.extend(vendidos)
            elif( fonte == 'olx'):
                novos, vendidos = olx.getDados(interesses)
                carros_novos.extend(novos)
                id_carros_vendidos.extend(vendidos)

        #Faz algo com os carros novos
        print('novos = [', end=' ,')
        for carro in carros_novos:
            print(carro.getID(), end=' ,')
        print(']\n')

        # faz algo com os carros que foram vendidos
        print("vendidos = "+str(id_carros_vendidos) )
