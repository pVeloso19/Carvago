from BaseDados.DBConexao import connectToDB

from Users.Interesse import Interesse
from Users.User import User


class UserDAO:

    __instance = None

    @classmethod
    def instance(user):
        if user.__instance is None:
            user.__instance = user()
        return user.__instance

    def getUserByEmail(self, email: str) -> User:
        _, cursor = connectToDB()

        query = """
            SELECT * FROM carvago.User 
                where email = '%s';
        """ % (email)
            
        try:
            cursor.execute(query)
            result = cursor.fetchone()

            id = int(result[0])
            nome = result[1]
            email = result[2]
            password = result[3]

            return User(id, nome, email, password)
        except:
            return None
    
    def register(self, user: User) -> int:
        
        connection, cursor = connectToDB()
        
        # falta verificar se o user já existe
        existe = False

        if ( (not existe) and user.getIdUser() <= 0):
            
            query = """
                INSERT INTO carvago.User
                    VALUES 
                        (default, %s, '%s', '%s');
            """ % (user.getNome(), user.getEmail(), user.getPassword())

            cursor.execute(query)
            connection.commit()

            query = """
                SELECT LAST_INSERT_ID();
            """

            cursor.execute(query)
            r = cursor.fetchone()

            return int(r[0])

        else:
            return user.getIdUser()

    def getInteressesUser(self, id_user: int) -> list:
        _, cursor = connectToDB()

        query = """
            SELECT * FROM carvago.Interesse
	            WHERE User_idUser = %s;
        """ % (str(id_user))
            
        cursor.execute(query)

        interesses = []
        for r in cursor:
            
            id_user = int(r[0])
            marca = r[1]
            modelo = r[2]
            fonte = r[3]

            i = Interesse(marca, modelo, fonte, id_user)

            interesses.append(i)
        
        return interesses
    
    def getALLInteresses(self) -> list:
        _, cursor = connectToDB()

        query = """
            SELECT distinct Marca, Modelo, Fonte FROM carvago.Interesse;
        """
            
        cursor.execute(query)

        interesses = []
        for r in cursor:
            
            marca = r[0]
            modelo = r[1]
            fonte = r[2]

            i = Interesse(marca, modelo, fonte)

            interesses.append(i)
        
        return interesses

    def adicionarCarroFavorito(self, id_user : int, id_carro : int):
        connection, cursor = connectToDB()

        query = """
            INSERT INTO Favorito
	            VALUES 
                    (%s, %s);
        """ % (str(id_user), str(id_carro))

        cursor.execute(query)
        connection.commit()
    
    def removeCarroFavorito(self, id_user : int, id_carro : int):
        connection, cursor = connectToDB()

        query = """
            DELETE FROM carvago.Favorito
	            WHERE User_idUser = %s and Carros_idCarros = %s;
        """ % (str(id_user), str(id_carro))

        cursor.execute(query)
        connection.commit()