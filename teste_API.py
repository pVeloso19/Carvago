import requests

"""
##### TODO #####

# Adicionar Interesse -> Id user, Interesse, Filtro Notificacao

# Remover Interesse -> Id user, ID Interesse, Filtro Notificacao

# Logout -> Id user

# Criar User
"""


#############################################
#               TESTE
#############################################

# 1) Login

response = requests.get( "http://localhost:5000/login", params={'email':'miguelveloso@mail.pt', 'password':'Pedro1234'} )
dados = response.json()

identificador = int(dados['resultado'])

print(identificador)

# 3) Todos os carros para um interesse
#response = requests.get( "http://localhost:5000/AllCars", params={'ID':identificador, 'marca':'ford', 'modelo':'focus'} )
#dados = response.json()

#print(dados)

# 4) Todos os carros não vistos
#response = requests.get( "http://localhost:5000/AllCarsNotSee", params={'ID':identificador} )
#dados = response.json()

#print(dados)

# 5) Todos os carros nos favoritos
#response = requests.get( "http://localhost:5000/AllFavoriteCars", params={'ID':identificador} )
#dados = response.json()

#print(dados)

# 6) Adiciona Interesse User
response = requests.get( "http://localhost:5000/AddInteresse", params={'ID':identificador, 'Marca':'VW2' , 'Modelo':'GOLF', 'AnoMinimo':2020, 'AnoMaximo':'', 'PrecoMinimo':'', 'PrecoMaximo':22000, 'Combustivel':'GASOLINA', 'KMMinimo':'', 'KMMaximo':''} )
dados = response.json()

print(dados)

# 2) Interesses de um user

response = requests.get( "http://localhost:5000/InteressesUser", params={'ID':identificador} )
dados = response.json()

print(dados)