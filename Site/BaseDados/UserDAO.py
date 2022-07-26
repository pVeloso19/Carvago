from BaseDados.DBConexao import connectToDB

from Users.FiltrosNotificacoes import FiltrosNotificacoes
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
    
    def getData(self, id_user: int) -> dict:
        _, cursor = connectToDB()

        query = """
            SELECT * FROM carvago.User 
                where idUser = '%s';
        """ % (str(id_user))
            
        try:
            cursor.execute(query)
            result = cursor.fetchone()

            res = {}
            res['nome'] = result[1]
            res['email'] = result[2]
            res['email_validado'] = False

            return res
        except:
            return None

    def register(self, user: User) -> int:
        
        connection, cursor = connectToDB()
        
        query = """
            INSERT INTO carvago.User
                VALUES 
                    (default, '%s', '%s', '%s');
        """ % (user.getNome(), user.getEmail(), user.getPassword())

        cursor.execute(query)
        connection.commit()

        query = """
            SELECT LAST_INSERT_ID();
        """

        cursor.execute(query)
        r = cursor.fetchone()

        return int(r[0])

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

    def addFiltroNotificacaoUser(self, id_user, filtrosNot : FiltrosNotificacoes) -> int:
        connection, cursor = connectToDB()
        
        query = """
            INSERT INTO carvago.Filtros_Notificacao
	            VALUES
                    (default, %s, %s, %s, %s, '%s', %s, %s);
        """ % ( filtrosNot.getAnoMinimo(), filtrosNot.getAnoMaximo(), filtrosNot.getPrecoMinimo(),
                filtrosNot.getPrecoMaximo(), filtrosNot.getCombustivel(), filtrosNot.getKMMinimo(), filtrosNot.getKMMaximo() )

        cursor.execute(query)
        connection.commit()

        query = """
            SELECT LAST_INSERT_ID();
        """

        cursor.execute(query)
        r = cursor.fetchone()

        return int(r[0])

    def addInteresseUser(self, id_user : int, interesses : list, id_filtro_notificacao : int) -> bool:
        connection, cursor = connectToDB()
        
        idFiltro = 'NULL' if (id_filtro_notificacao < 0) else str(id_filtro_notificacao)
        for interesse in interesses:
            query = """
                INSERT INTO carvago.Interesse
                    VALUES
                        (%s, '%s', '%s', '%s', %s)
            """ % ( str(id_user),  interesse.getMarca().lower(), interesse.getModelo().lower(), interesse.getFonte(), idFiltro)
            
            cursor.execute(query)
            connection.commit()
        
        return True


