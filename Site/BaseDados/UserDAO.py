from matplotlib.pyplot import connect
from mysql.connector import connection
from DBConexao import connectToDB
from Users.User import User


class UserDAO:

    __instance = None

    @classmethod
    def instance(user):
        if user.__instance is None:
            user.__instance = user()
        return user.__instance

    def checkUser(self, user: User) -> int:
        _, cursor = connectToDB()

        email = user.getEmail()
        password = user.getPassword()

        if (email != -1 and password != -1):
            query = """
                        SELECT email FROM User where email = '%s';
                    """ % (email)
            cursor.execute(query)
            result = cursor.fetchone()[0]

            if result < 0:
                return -2  # email não existe
            else:
                queryPass = """
                                SELECT password FROM User where email = '%s';
                            """ % (email)
                cursor.execute(queryPass)
                res = cursor.fetchone()[0]

                if (res == password):
                    return 1  # user existe
                else:
                    return -2  # password não coincide
        else:
            return -3  # algum campo vem vazio

    def put(self, user: User) -> int:
        connection, cursor = connectToDB()

        # falta verificar se o user já existe

        if (user.getIdUser() == -1):
            query = """
                        INSERT INTO User (Nome, Email, Password)
                        VALUES (%s, %s, %s);
                    """
            values = (user.getNome, user.getEmail, user.getPassword)

            try:
                cursor.execute(query, values)
                connection.commit()
            except:
                return -1

        else:
            return -1
