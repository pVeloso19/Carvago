import threading
from REST.REST import REST_API

def main0():
    import time
    from API.APIFacade import APIFacade
    
    apiFacade = APIFacade()
    while True:
        #apiFacade.getDados()
        print('INICIOU\n\n')
        time.sleep(60*60*2) # De 2 em 2 horas atualiza os dados

def main():
    # Inicia o modulo para obter os dados de x em x horas
    threading.Thread(target = main0, args=(), daemon=True).start()
    
    # Inicia a API REST
    rest_api = REST_API()
    rest_api.init()



# Executa a função main
if __name__ == '__main__':
    main()