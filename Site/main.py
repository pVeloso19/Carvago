import threading
from REST.REST import REST_API
from API.APIFacade import APIFacade
import getopt, sys

def main0(apiFacade : APIFacade):
    print('Daemon responsável por obter os dados iniciado.')
    i = 2
    import time
    while True:
        time.sleep(60*60*2) # De 2 em 2 horas atualiza os dados
        print(f'A obter os dados pela {i}ª vez.')
        apiFacade.getDados()
        i += 1

def componenteGetData():
    apiFacade = APIFacade()
    
    print('A obter os dados pela 1ª vez.')
    apiFacade.getDados()
    
    # Inicia o modulo para obter os dados de x em x horas
    threading.Thread(target = main0, args=(apiFacade, ), daemon=True).start()

def main(args):

    lst = sys.argv[1:]
    options = "g:"
    long_options = ["getdados="]

    getdados = False

    try:
        arguments, _ = getopt.getopt(lst, options, long_options)
        _, valor = arguments[0]
        getdados = valor.upper() == 'TRUE'
    except:
        pass

    if (getdados):
        componenteGetData()
    
    # Inicia a API REST
    rest_api = REST_API()
    rest_api.init()



# Executa a função main
if __name__ == '__main__':
    main(sys.argv)