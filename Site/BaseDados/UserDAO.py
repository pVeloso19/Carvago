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
            res['email_validado'] = True if(int(result[5]) == 1) else False
            res['aceitou_notificacoes'] = True if(int(result[6]) == 1) else False

            return res
        except:
            return None

    def register(self, user: User, token : dict) -> int:
        
        connection, cursor = connectToDB()

        id_token = 'NULL'
        an = 'FALSE'
        if token is not None:
            ept = 'NULL' if (token['expirationTime'] is None) else f"'{token['expirationTime']}'"
            query = """
                INSERT INTO carvago.PushInfo
                    VALUES 
                        (default, '%s', '%s', '%s', %s);
            """ % (token['endpoint'], token['keys']['p256dh'], token['keys']['auth'], ept)

            cursor.execute(query)
            connection.commit()

            query = """
                SELECT LAST_INSERT_ID();
            """

            cursor.execute(query)
            r = cursor.fetchone()

            id_token = str(int(r[0]))
            an = 'TRUE'
        
        query = """
            INSERT INTO carvago.User
                VALUES 
                    (default, '%s', '%s', '%s', %s, FALSE, %s);
        """ % (user.getNome(), user.getEmail(), user.getPassword(), id_token, an)

        cursor.execute(query)
        connection.commit()

        query = """
            SELECT LAST_INSERT_ID();
        """

        cursor.execute(query)
        r = cursor.fetchone()

        return int(r[0])
    
    def registerToken(self, id_user : int, token : dict):
        connection, cursor = connectToDB()
        
        ept = 'NULL' if (token['expirationTime'] is None) else f"'{token['expirationTime']}'"
        query = """
            INSERT INTO carvago.PushInfo
                VALUES 
                    (default, '%s', '%s', '%s', %s);
        """ % (token['endpoint'], token['keys']['p256dh'], token['keys']['auth'], ept)

        cursor.execute(query)

        query = """
            UPDATE carvago.User
                SET aceitouNotificacoes = TRUE
                WHERE idUser = %s;
        """ % (str(id_user))

        cursor.execute(query)
        connection.commit()

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

    def removeFiltrosNotificacoes(self, interesses : list, lista_id_filtros: list) -> bool:
        connection, cursor = connectToDB()
        
        from re import sub
        id_filtros = str(lista_id_filtros)
        id_filtros = sub('\[','(', id_filtros)
        id_filtros = sub('\]',')', id_filtros)

        for interesse in interesses:
            query = """
                DELETE FROM carvago.Filtros_Notificacao 
                    WHERE idFiltros IN %s
            """ % ( id_filtros )
            
            cursor.execute(query)
            connection.commit()
        
        return True
    
    def removeInteresseUser(self, id_user : int, interesses : list) -> list:
        connection, cursor = connectToDB()

        query = """
            SELECT DISTINCT Filtros_Notificacao_idFiltros FROM carvago.Interesse 
                WHERE User_idUser = %s AND Marca='%s' AND Modelo='%s'
        """ % ( str(id_user),  interesses[0].getMarca().lower(), interesses[0].getModelo().lower())

        cursor.execute(query)

        res = []
        for r in cursor:
            res.append(int(r[0]))

        for interesse in interesses:
            query = """
                DELETE FROM carvago.Interesse 
	                WHERE User_idUser = %s AND Marca='%s' AND Modelo='%s'
            """ % ( str(id_user),  interesse.getMarca().lower(), interesse.getModelo().lower())
            
            cursor.execute(query)
            connection.commit()
        
        return res
    
    def getTokenUser(self, id_user : int) -> dict:
        connection, cursor = connectToDB()

        query = """
            SELECT endpoint, p256dh, auth, expirationTime FROM carvago.PushInfo as p
                JOIN carvago.User as u on u.idPushInfo=p.idPushInfo
                    WHERE u.idUser = %s;
        """ % ( str(id_user) )

        cursor.execute(query)
        r = cursor.fetchone()
        
        res = None
        if (r is not None):
            res = {}
            res['endpoint'] = r[0]
            res['expirationTime'] = None if r[3] == 'NULL' else r[3]
            temp = {}
            temp['p256dh'] = r[1]
            temp['auth'] = r[2]
            res['keys'] = temp
        
        return res
