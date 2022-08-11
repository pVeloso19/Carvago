from API.StandVirtualFont import StandVirtualGather
from API.OlxFont import OLXGather
from Users.UserFacade import UserFacade

import time
from pywebpush import webpush
import json, os

class APIFacade:
    def __init__(self):
        DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH = os.path.join(os.getcwd(),"private_key.txt")
        
        self.VAPID_PRIVATE_KEY = open(DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH, "r+").readline().strip("\n")
        self.VAPID_CLAIMS = {
            "sub": "mailto:develop@raturi.in"
        }

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
            time.sleep(60*5)

        #Faz algo com os carros novos (var carros_novos)
        ids_users_notificar = [9]

        for id_user in ids_users_notificar:
            message = "Existe um novo carro do seu interesse disponivel."

            temp = userFacade.getTokenUser(id_user)

            if (temp is None):
                pass
            else:
                token = json.dumps(temp)
                try:
                    token = json.loads(token)
                    webpush(
                        subscription_info=token,
                        data=message,
                        vapid_private_key=self.VAPID_PRIVATE_KEY,
                        vapid_claims=self.VAPID_CLAIMS
                    )
                except Exception as e:
                    print("error", e)

        # faz algo com os carros que foram vendidos?
        #print("vendidos = "+str(id_carros_vendidos) )
