
from BaseDados.UserDAO import UserDAO
from Users.User import User
from Users.Interesse import Interesse
from Users.FiltrosNotificacoes import FiltrosNotificacoes


class UserFacade:

    def __init__(self):
        pass

    # Método responsável por efetuar o login de um utilizador
    # Realiza o login através do email e password
    # Retorna um inteiro <0 se erro ou >0 se sucesso
        # -1 Falha nos campos
        # -2 password inválida
        # -3 email inválido
        # maior que zero sucesso. O valor corresponde ao id do utilizador
    def login(self, email : str, password : str) -> int:
        
        if(password is None or password==''):
            return -1

        if(email is None or email==''):
            return -1
        
        user_DAO = UserDAO.instance()

        user = user_DAO.getUserByEmail(email)

        if(user is not None):
            
            if(user.getPassword() == password):
                return user.getIdUser()
            else:
                return -2
        
        else:
            return -3

    def getInteressesUser(self, id_user = -1) -> dict:
        res = {}
        user_DAO = UserDAO.instance()
        
        if(id_user <= 0):
            lista = user_DAO.getALLInteresses()
        else:
            lista = user_DAO.getInteressesUser(id_user)

        for i in lista:
            fonte = i.getFonte()
            
            if(fonte not in res):
                res[fonte] = []
            
            res[fonte].append( (i.getMarca(), i.getModelo()) )

        return res

    def addInteresse(self, id_user : int, interesses : list, filtro : FiltrosNotificacoes) -> bool:
        user_DAO = UserDAO.instance()

        id_filtro = -1
        if(filtro is not None):
            id_filtro = user_DAO.addFiltroNotificacaoUser(id_user, filtro)
        
        user_DAO.addInteresseUser(id_user, interesses, id_filtro)

        return True
    
    def removeInteresse(self, id_user : int, interesses : list) -> bool:
        #apagar filtros de notificação

        #apagar os interesses

        return True

    def addFavorito(self, id_user : int, id_carro : int) -> bool:
        user_DAO = UserDAO.instance()
        user_DAO.adicionarCarroFavorito(id_user, id_carro)
        return True

    def removeFavorito(self, id_user : int, id_carro : int) -> bool:
        user_DAO = UserDAO.instance()
        user_DAO.removeCarroFavorito(id_user, id_carro)
        return True
    
    # Método responsável por efetuar o registo de um utilizador
    # Retorna um inteiro <0 se erro ou >0 se sucesso
        # -1 Falha nos campos
        # -2 password inválida
        # -3 email inválido
        # maior que zero sucesso. O valor corresponde ao id do utilizador
    def registar(self, nome : str, email : str, password : str) -> int:
        user = User(-3, nome, email, password)
        user_DAO = UserDAO.instance()
        return user_DAO.register(user)
