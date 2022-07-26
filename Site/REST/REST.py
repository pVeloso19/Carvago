from flask import Flask, request, jsonify, render_template

from Carros.CarrosFacade import CarrosFacade
from Users.UserFacade import UserFacade

class REST_API:
    
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['JSON_AS_ASCII'] = False

        self.__carrosFacade = CarrosFacade()
        self.__userFacade = UserFacade()

    def init(self):
        self.define_PATH()
        self.app.run(debug=True, host='0.0.0.0', port=5000)

    def define_PATH(self):
        
        @self.app.route('/login', methods=['GET']) 
        def login():
            
            email = request.args.get('email')
            password = request.args.get('password')
            
            res = self.__userFacade.login(email, password)

            response = jsonify(dict( resultado = res))
            response.headers.add('Access-Control-Allow-Origin', '*')

            return response
        
        @self.app.route('/create', methods=['GET']) 
        def create():
            
            nome = request.args.get('nome')
            email = request.args.get('email')
            password = request.args.get('password')
            
            res = self.__userFacade.createAccount(nome, email, password)

            response = jsonify(dict( resultado = res))
            response.headers.add('Access-Control-Allow-Origin', '*')

            return response
        
        @self.app.route('/userData', methods=['GET']) 
        def userData():
            
            id_user = int(request.args.get('ID'))
            
            res = self.__userFacade.getUserData(id_user)

            response = jsonify(dict( resultado = res))
            response.headers.add('Access-Control-Allow-Origin', '*')

            return response
        
        @self.app.route('/InteressesUser', methods=['GET']) 
        def getInteresses():
            
            id_user = int(request.args.get('ID'))
            
            res = self.__userFacade.getInteressesUser(id_user)

            response = jsonify(res)
            response.headers.add('Access-Control-Allow-Origin', '*')

            return response
        
        @self.app.route('/AllCars', methods=['GET']) 
        def getAllCarsByTarget():
            
            id_user = int(request.args.get('ID'))
            marca = request.args.get('marca')
            modelo = request.args.get('modelo')
            
            res = self.__carrosFacade.getTodosCarrosPorInteresse(id_user, marca, modelo)

            response = jsonify(dict( carros = res))
            response.headers.add('Access-Control-Allow-Origin', '*')

            return response
        
        @self.app.route('/AllCarsNotSee', methods=['GET']) 
        def getAllCarsNotSee():
            
            id_user = int(request.args.get('ID'))
            
            res = self.__carrosFacade.getTodosCarrosNaoVistos(id_user)
            
            response = jsonify(dict( carros = res))
            response.headers.add('Access-Control-Allow-Origin', '*')

            return response
        
        @self.app.route('/AllFavoriteCars', methods=['GET']) 
        def getAllFavoriteCars():
            
            id_user = int(request.args.get('ID'))
            
            res = self.__carrosFacade.getTodosCarrosFavoritos(id_user)
            
            response = jsonify(dict( carros = res))
            response.headers.add('Access-Control-Allow-Origin', '*')

            return response
        
        @self.app.route('/AddFavorito', methods=['GET']) 
        def addFavorito():
            
            id_user = int(request.args.get('ID'))
            id_carro = int(request.args.get('IDCarro'))
            
            res = self.__userFacade.addFavorito(id_user, id_carro)
            
            response = jsonify(dict( resultado = res))
            response.headers.add('Access-Control-Allow-Origin', '*')

            return response
        
        @self.app.route('/RemoveFavorito', methods=['GET']) 
        def removeFavorito():
            
            id_user = int(request.args.get('ID'))
            id_carro = int(request.args.get('IDCarro'))
            
            res = self.__userFacade.removeFavorito(id_user, id_carro)
            
            response = jsonify(dict( resultado = res))
            response.headers.add('Access-Control-Allow-Origin', '*')

            return response
        
        @self.app.route('/AddInteresse', methods=['GET']) 
        def AddInteresse():
            from Users.FiltrosNotificacoes import FiltrosNotificacoes
            from Users.Interesse import Interesse

            id_user = int(request.args.get('ID'))

            fontes = ['stand-virtual', 'olx']
            interesses = []
            for fonte in fontes:
                interesse = Interesse(request.args.get('Marca'), request.args.get('Modelo'), fonte, ID_User=id_user )
                interesses.append(interesse)

            filtro = FiltrosNotificacoes(
                -1, 
                request.args.get('AnoMinimo'), 
                request.args.get('AnoMaximo'), 
                request.args.get('PrecoMinimo'),
                request.args.get('PrecoMaximo'),
                request.args.get('Combustivel'),
                request.args.get('KMMinimo'),
                request.args.get('KMMaximo')
            )
            
            res = self.__userFacade.addInteresse( id_user, interesses, filtro)
            
            response = jsonify(dict( resultado = res))
            response.headers.add('Access-Control-Allow-Origin', '*')

            return response
        
        @self.app.route('/RemoveInteresse', methods=['GET']) 
        def RemoveInteresse():
            from Users.Interesse import Interesse

            id_user = int(request.args.get('ID'))

            fontes = ['stand-virtual', 'olx']
            interesses = []
            for fonte in fontes:
                interesse = Interesse(request.args.get('Marca'), request.args.get('Modelo'), fonte, ID_User=id_user )
                interesses.append(interesse)

            res = self.__userFacade.removeInteresse(id_user, interesses)
            
            response = jsonify(dict( resultado = res))
            response.headers.add('Access-Control-Allow-Origin', '*')

            return response
        
        @self.app.route('/AllCarsAvailable', methods=['GET']) 
        def AllCarsAvailable():
            from Users.FiltrosNotificacoes import FiltrosNotificacoes

            id_user = int(request.args.get('ID'))
            modelo = request.args.get('Modelo')

            ordem = request.args.get('Ordem')

            marca = request.args.get('Marca')
            combustivel = request.args.get('Combustivel')
            
            from re import split
            marca = '' if(marca == '') else split(',', marca)
            combustivel = '' if(combustivel == '') else split(',', combustivel)

            print(marca)

            filtro = FiltrosNotificacoes(
                -1, 
                request.args.get('AnoMinimo'), 
                request.args.get('AnoMaximo'), 
                request.args.get('PrecoMinimo'),
                request.args.get('PrecoMaximo'),
                combustivel,
                request.args.get('KMMinimo'),
                request.args.get('KMMaximo')
            )
            
            res, pages = self.__carrosFacade.getTodosCarrosAvailable(id_user, marca, modelo, filtro, int(request.args.get('Pagina')), ordem )

            response = jsonify(dict( carros = res, paginas = pages))
            response.headers.add('Access-Control-Allow-Origin', '*')

            return response
