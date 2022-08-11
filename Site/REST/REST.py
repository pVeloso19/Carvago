from flask import Flask, request, Response, jsonify, render_template, send_from_directory
from flask_cors import CORS, cross_origin
#@cross_origin(origin='*',headers=['Content-Type','Authorization'])

from pywebpush import webpush

import json, os

from Carros.CarrosFacade import CarrosFacade
from Users.UserFacade import UserFacade

class REST_API:
    
    def __init__(self):
        self.app = Flask(__name__)
        
        self.cors = CORS(self.app, resources={r"/foo": {"origins": "*"}})
        self.app.config['CORS_HEADERS'] = 'Content-Type'
        
        self.app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
        self.app.config['JSON_AS_ASCII'] = False

        self.__carrosFacade = CarrosFacade()
        self.__userFacade = UserFacade()

        self.DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH = os.path.join(os.getcwd(),"private_key.txt")
        self.DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH = os.path.join(os.getcwd(),"public_key.txt")

        self.VAPID_PRIVATE_KEY = open(self.DER_BASE64_ENCODED_PRIVATE_KEY_FILE_PATH, "r+").readline().strip("\n")
        self.VAPID_PUBLIC_KEY = open(self.DER_BASE64_ENCODED_PUBLIC_KEY_FILE_PATH, "r+").read().strip("\n")

        self.VAPID_CLAIMS = {
            "sub": "mailto:develop@raturi.in"
        }

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

        @self.app.route("/subscription", methods=["GET", "POST"])
        def subscription():
            """
                POST creates a subscription
                GET returns vapid public key which clients uses to send around push notification
            """

            if request.method == "GET":
                return Response(response=json.dumps({"public_key": self.VAPID_PUBLIC_KEY}),
                    headers={"Access-Control-Allow-Origin": "*"}, content_type="application/json")

            try:
                subscription_token = request.get_json("subscription_token")
                subscription_token = subscription_token['subscription_token']
                subscription_token = json.loads(subscription_token)
            except:
                subscription_token = None

            if subscription_token is not None:
                id_user = int(request.args.get('ID'))
                self.__userFacade.registerToken(id_user, subscription_token)

            return Response(status=201, headers={"Access-Control-Allow-Origin": "*"}, mimetype="application/json")
        
        @self.app.route('/<path:filename>', methods=['GET', 'POST'])
        def download(filename):
            return send_from_directory('templates/static',filename, as_attachment=True)

        @self.app.route('/')
        def hello():
            return render_template('index.html')

        @self.app.route('/create', methods=['POST']) 
        def create():
            
            nome = request.args.get('nome')
            email = request.args.get('email')
            password = request.args.get('password')

            try:
                subscription_token = request.get_json("subscription_token")
                subscription_token = subscription_token['subscription_token']
                subscription_token = json.loads(subscription_token)
            except:
                subscription_token = None
            
            res = self.__userFacade.createAccount(nome, email, password, subscription_token)

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
        
        @self.app.route('/ImagensCars', methods=['GET']) 
        def ImagensCars():
            
            res = self.__carrosFacade.getImagensCarros()

            response = jsonify(dict( images = res))
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

        @self.app.route("/push", methods=['POST'])
        @cross_origin(origin='*',headers=['Content-Type','Authorization'])
        def push():
            message = "Novo carro disponivel!!!"

            id_user = int(request.args.get('ID'))
            
            token = self.__userFacade.getTokenUser(id_user)

            if (token is None):
                return jsonify({'failed':str(e)})

            try:
                _ = webpush(
                    subscription_info=token,
                    data=message,
                    vapid_private_key=self.VAPID_PRIVATE_KEY,
                    vapid_claims=self.VAPID_CLAIMS
                )
                return jsonify({'success':1})
            except Exception as e:
                print("error",e)
                return jsonify({'failed':str(e)})