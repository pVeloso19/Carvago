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

            return jsonify(dict( resultado = res))
        
        @self.app.route('/InteressesUser', methods=['GET']) 
        def getInteresses():
            
            id_user = int(request.args.get('ID'))
            
            res = self.__userFacade.getInteressesUser(id_user)

            return jsonify(res)
        
        @self.app.route('/AllCars', methods=['GET']) 
        def getAllCarsByTarget():
            
            id_user = int(request.args.get('ID'))
            marca = request.args.get('marca')
            modelo = request.args.get('modelo')
            
            res = self.__carrosFacade.getTodosCarrosPorInteresse(id_user, marca, modelo)

            return jsonify(dict( carros = res))
        
        @self.app.route('/AllCarsNotSee', methods=['GET']) 
        def getAllCarsNotSee():
            
            id_user = int(request.args.get('ID'))
            
            res = self.__carrosFacade.getTodosCarrosNaoVistos(id_user)
            
            return jsonify(dict( carros = res))
        
        @self.app.route('/AllFavoriteCars', methods=['GET']) 
        def getAllFavoriteCars():
            
            id_user = int(request.args.get('ID'))
            
            res = self.__carrosFacade.getTodosCarrosFavoritos(id_user)
            
            return jsonify(dict( carros = res))
        
        @self.app.route('/AddFavorito', methods=['GET']) 
        def addFavorito():
            
            id_user = int(request.args.get('ID'))
            id_carro = int(request.args.get('IDCarro'))
            
            res = self.__userFacade.addFavorito(id_user, id_carro)
            
            return jsonify(dict( resultado = res))
        
        @self.app.route('/RemoveFavorito', methods=['GET']) 
        def removeFavorito():
            
            id_user = int(request.args.get('ID'))
            id_carro = int(request.args.get('IDCarro'))
            
            res = self.__userFacade.removeFavorito(id_user, id_carro)
            
            return jsonify(dict( resultado = res))


#rest_api = REST_API()
#rest_api.init()


from API.StandVirtualFont import StandVirtualGather

#Inicia todas as fontes
stand_virtual = StandVirtualGather()

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

#Faz algo com os carros novos
print('novos = [')
for carro in carros_novos:
    print(carro.getID(), end=' ,')
print(']\n')

# faz algo com os carros que foram vendidos
print("vendidos = "+str(id_carros_vendidos) )




# Executa a função main
"""
if __name__ == '__main__':
    main()
"""