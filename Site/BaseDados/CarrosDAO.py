
from BaseDados.DBConexao import connectToDB
from Carros.Carro import Carro
from Users.FiltrosNotificacoes import FiltrosNotificacoes

class CarrosDAO:
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def insertCarro(self, carro : Carro) -> int:
        
        connection, cursor = connectToDB()

        query = """
            INSERT INTO carvago.Carros
                VALUES
                    (default, '%s', '%s', '%s', '%s', '%s', '%s', %s, %s, %s, %s, '%s', '%s', '%s', %s, '%s', '%s', %s, '%s', '%s', '%s', %s, '%s',  now())
                ON DUPLICATE KEY UPDATE 
                    Anunciante = VALUES(Anunciante),
                    Marca = VALUES(Marca),
                    Modelo = VALUES(Modelo),
                    Versao = VALUES(Versao),
                    Combustivel = VALUES(Combustivel),
                    Mes_Registo = VALUES(Mes_Registo),
                    Ano = VALUES(Ano),
                    Quilometros = VALUES(Quilometros),
                    Cilindrada = VALUES(Cilindrada),
                    Potencia = VALUES(Potencia),
                    Cor = VALUES(Cor),
                    Tipo_Cor = VALUES(Tipo_Cor),
                    Tipo_Caixa = VALUES(Tipo_Caixa),
                    Num_Portas = VALUES(Num_Portas),
                    Origem = VALUES(Origem),
                    Condicao = VALUES(Condicao),
                    Preco = VALUES(Preco),
                    Link_foto = VALUES(Link_foto),
                    Titulo = VALUES(Titulo),
                    Link_anuncio = VALUES(Link_anuncio),
                    ID_Anuncio = VALUES(ID_Anuncio),
                    Fonte = VALUES(Fonte);
        """%(
                carro.getAnunciante(), 
                carro.getMarca(), 
                carro.getModelo(), 
                carro.getVersao(), 
                carro.getCombustivel(),
                carro.getMes_Registo(),
                str(carro.getAno()),
                str(carro.getQuilometros()),
                str(carro.getCilindrada()),
                str(carro.getPotencia()),
                carro.getCor(),
                carro.getTipo_Cor(),
                carro.getTipo_Caixa(),
                str(carro.getNum_Portas()),
                carro.getOrigem(),
                carro.getCondicao(),
                str(carro.getPreco()),
                carro.getLink_foto(),
                carro.getTitulo(),
                carro.getLink_anuncio(),
                str(carro.getIDAnuncio()),
                carro.getFonte()
        )

        """
        print(query)
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        """

        cursor.execute(query)
        connection.commit()

        query = """
            SELECT LAST_INSERT_ID();
        """

        cursor.execute(query)
        r = cursor.fetchone()

        return int(r[0])

    def getAllCarrosByMarcaANDModelo(self, marca : str, modelo : str, id_user : int) -> list:
        _, cursor = connectToDB()

        query = """
            select * from carvago.Carros
                where Marca = '%s' and Modelo = '%s'
                ORDER BY Data DESC;
        """%(marca, modelo)

        cursor.execute(query)

        carros = []
        for r in cursor:
            id = int(r[0])
            anunciante = r[1]
            versao = r[4]
            combustivel = r[5]
            mes_registo = r[6]
            ano = int(r[7])
            quilometros = int(r[8])
            cilindrada = int(r[9])
            potencia = int(r[10])
            cor = r[11]
            tipo_cor = r[12]
            tipo_caixa = r[13]
            num_portas = int(r[14])
            origem = r[15]
            condicao = r[16]
            preco = float(r[17])
            link_foto = r[18]
            titulo = r[19]
            link_anuncio = r[20]
            id_anuncio = int(r[21])
            fonte = r[22]

            fav = self.isCarroInFavoriteUser(id_user, id)

            carro = Carro( anunciante, marca, modelo, versao, combustivel, mes_registo, ano, quilometros, cilindrada, potencia, cor, 
                           tipo_cor, tipo_caixa, num_portas, origem, condicao, preco, link_foto, titulo, link_anuncio, id_anuncio, fonte, ID=id, Favorito=fav)
            
            carros.append(carro)

        return carros
    
    def getAllIDAnuncioCarrosByMarcaANDModeloANDFonte(self, marca : str, modelo : str, fonte : str) -> list:
        _, cursor = connectToDB()

        query = """
            select ID_Anuncio from carvago.Carros
                where Marca = '%s' and Modelo = '%s' and Fonte='%s';
        """%(marca, modelo, fonte)

        cursor.execute(query)

        ids = []
        for r in cursor:
            ids.append(int(r[0]))

        return ids
    
    def deleteCarroByIDAnuncioANDFonte(self, id_anuncio : int, fonte : str) -> bool:
        connection, cursor = connectToDB()

        #Obtem todos os ids desses carros
        query = """
            SELECT idCarros FROM carvago.Carros
	            WHERE ID_Anuncio = %s and Fonte = '%s';
        """%(str(id_anuncio), fonte)

        cursor.execute(query)

        ids_carros = []
        for r in cursor:
            ids_carros.append(int(r[0]))
        
        #Apaga do nao vistos
        for id_carro in ids_carros:
            query = """
                DELETE FROM carvago.Carros_Nao_Vistos
	                WHERE Carros_idCarros = %s;
            """%(str(id_carro))

            cursor.execute(query)

        #apaga dos favoritos
        for id_carro in ids_carros:
            query = """
                DELETE FROM carvago.Favorito
	                WHERE Carros_idCarros = %s;
            """%(str(id_carro))

            cursor.execute(query)
        
        #apaga dos carros
        for id_carro in ids_carros:
            query = """
                DELETE FROM carvago.Carros
	                WHERE idCarros = %s;
            """%(str(id_carro))

            cursor.execute(query)

        connection.commit()
        return True
    
    def updateCarroByIDAnuncioANDFonte(self, carro : Carro) -> bool:
        connection, cursor = connectToDB()

        query = """
            UPDATE carvago.Carros SET 
                Quilometros = %s,
                Preco = %s,
                Link_foto = '%s',
                Link_anuncio = '%s'
            WHERE ID_Anuncio = %s and Fonte = '%s';
        """ % (
            str(carro.getQuilometros()),
            str(carro.getPreco()),
            carro.getLink_foto(),
            carro.getLink_anuncio(),
            str(carro.getIDAnuncio()),
            carro.getFonte()
        )

        cursor.execute(query)
        connection.commit()

        return True

    def insertCarrosNaoVisto(self, id_carro : int, carro : Carro) -> bool:
        
        connection, cursor = connectToDB()

        query = """
            SELECT User_idUser FROM carvago.Interesse
	            WHERE Marca = '%s' and Modelo = '%s' and Fonte = '%s';
        """%(carro.getMarca(), carro.getModelo(), carro.getFonte())

        cursor.execute(query)

        ids_users = []
        for r in cursor:
            ids_users.append(int(r[0]))
        
        for id_user in ids_users:
            query = """
                INSERT INTO carvago.Carros_Nao_Vistos
	                values (%s, %s);
            """%(str(id_user), str(id_carro))

            cursor.execute(query)
            connection.commit()
        
        return True
    
    def getAllCarrosNaoVistos(self, id_user : int) -> list:
        _, cursor = connectToDB()

        query = """
            select * FROM carvago.Carros_Nao_Vistos
	            WHERE User_idUser = %s;
        """%( str(id_user) )

        cursor.execute(query)

        carros_nao_vistos = []
        for r in cursor:
            carros_nao_vistos.append( int(r[1]) )

        if(not carros_nao_vistos):
            return []

        from re import sub
        carros_nao_vistos = str(carros_nao_vistos)
        carros_nao_vistos = sub('\[','(', carros_nao_vistos)
        carros_nao_vistos = sub('\]',')', carros_nao_vistos)

        query = """
            select * from carvago.Carros
                WHERE idCarros in %s
                ORDER BY Data DESC;
        """%(carros_nao_vistos)

        cursor.execute(query)
        carros = []
        for r in cursor:
            id = int(r[0])
            anunciante = r[1]
            marca = r[2]
            modelo = r[3]
            versao = r[4]
            combustivel = r[5]
            mes_registo = r[6]
            ano = int(r[7])
            quilometros = int(r[8])
            cilindrada = int(r[9])
            potencia = int(r[10])
            cor = r[11]
            tipo_cor = r[12]
            tipo_caixa = r[13]
            num_portas = int(r[14])
            origem = r[15]
            condicao = r[16]
            preco = float(r[17])
            link_foto = r[18]
            titulo = r[19]
            link_anuncio = r[20]
            id_anuncio = int(r[21])
            fonte = r[22]

            fav = self.isCarroInFavoriteUser(id_user, id)

            carro = Carro( anunciante, marca, modelo, versao, combustivel, mes_registo, ano, quilometros, cilindrada, potencia, cor, 
                           tipo_cor, tipo_caixa, num_portas, origem, condicao, preco, link_foto, titulo, link_anuncio, id_anuncio, fonte, ID=id, Favorito=fav)
            
            carros.append(carro)

        return carros

    def getAllCarrosFavoritos(self, id_user : int) -> list:
        _, cursor = connectToDB()

        query = """
            select * FROM carvago.Favorito
	            WHERE User_idUser = %s;
        """%( str(id_user) )

        cursor.execute(query)

        carros_favoritos = []
        for r in cursor:
            carros_favoritos.append( int(r[1]) )

        if(not carros_favoritos):
            return []

        from re import sub
        carros_favoritos = str(carros_favoritos)
        carros_favoritos = sub('\[','(', carros_favoritos)
        carros_favoritos = sub('\]',')', carros_favoritos)

        query = """
            select * from carvago.Carros
                WHERE idCarros in %s
                ORDER BY Data DESC;
        """%(carros_favoritos)

        cursor.execute(query)
        carros = []
        for r in cursor:
            id = int(r[0])
            anunciante = r[1]
            marca = r[2]
            modelo = r[3]
            versao = r[4]
            combustivel = r[5]
            mes_registo = r[6]
            ano = int(r[7])
            quilometros = int(r[8])
            cilindrada = int(r[9])
            potencia = int(r[10])
            cor = r[11]
            tipo_cor = r[12]
            tipo_caixa = r[13]
            num_portas = int(r[14])
            origem = r[15]
            condicao = r[16]
            preco = float(r[17])
            link_foto = r[18]
            titulo = r[19]
            link_anuncio = r[20]
            id_anuncio = int(r[21])
            fonte = r[22]

            carro = Carro( anunciante, marca, modelo, versao, combustivel, mes_registo, ano, quilometros, cilindrada, potencia, cor, 
                           tipo_cor, tipo_caixa, num_portas, origem, condicao, preco, link_foto, titulo, link_anuncio, id_anuncio, fonte, ID=id, Favorito=True)
            
            carros.append(carro)

        return carros

    def marcaCarrosComoVistos(self, id_user : int):
        connection, cursor = connectToDB()

        query = """
            DELETE FROM carvago.Carros_Nao_Vistos
	            WHERE User_idUser = %s;
        """%( str(id_user) )

        cursor.execute(query)
        connection.commit()

    def getAllCarrosInteresseByUtilizador(self, id_user : int):
        _, cursor = connectToDB()

        query = """
            SELECT * FROM carvago.Carros
	            WHERE (Marca, Modelo) in (SELECT Marca, Modelo FROM carvago.Interesse WHERE User_idUser=%s)
                ORDER BY Data DESC;
        """%(str(id_user))

        cursor.execute(query)

        carros = []
        for r in cursor:
            id = int(r[0])
            anunciante = r[1]
            marca = r[2]
            modelo = r[3]
            versao = r[4]
            combustivel = r[5]
            mes_registo = r[6]
            ano = int(r[7])
            quilometros = int(r[8])
            cilindrada = int(r[9])
            potencia = int(r[10])
            cor = r[11]
            tipo_cor = r[12]
            tipo_caixa = r[13]
            num_portas = int(r[14])
            origem = r[15]
            condicao = r[16]
            preco = float(r[17])
            link_foto = r[18]
            titulo = r[19]
            link_anuncio = r[20]
            id_anuncio = int(r[21])
            fonte = r[22]

            fav = self.isCarroInFavoriteUser(id_user, id)

            carro = Carro( anunciante, marca, modelo, versao, combustivel, mes_registo, ano, quilometros, cilindrada, potencia, cor, 
                           tipo_cor, tipo_caixa, num_portas, origem, condicao, preco, link_foto, titulo, link_anuncio, id_anuncio, fonte, ID=id, Favorito=fav)
            
            carros.append(carro)

        return carros

    def isCarroInFavoriteUser(self, id_user : int, id_carro : int) -> bool:
        _, cursor = connectToDB()

        query = """
            SELECT * FROM carvago.Favorito
	            WHERE User_idUser=%s AND Carros_idCarros=%s;
        """%(str(id_user), str(id_carro))

        cursor.execute(query)

        for _ in cursor:
            return True

        return False
    
    def getAllCarrosAvailable(self, id_user : int, marca : list, modelo : str, filtro : FiltrosNotificacoes, num_pag : int, ordem : str) -> list:
        _, cursor = connectToDB()

        ordemBY = 'ORDER BY Data DESC'

        if(ordem == 'Preço: Mais Baixo'):
            ordemBY = 'ORDER BY Preco ASC'
        elif(ordem == 'Preço: Mais Alto'):
            ordemBY = 'ORDER BY Preco DESC'
        elif(ordem == 'KM: Mais Baixo'):
            ordemBY = 'ORDER BY Quilometros ASC'
        elif(ordem == 'KM: Mais Alto'):
            ordemBY = 'ORDER BY Quilometros DESC'
        elif(ordem == 'Ano: Mais Baixo'):
            ordemBY = 'ORDER BY Ano ASC'
        elif(ordem == 'Ano: Mais Alto'):
            ordemBY = 'ORDER BY Ano DESC'
        
        from re import sub
        marcas = str(marca)
        marcas = sub('\[','(', marcas)
        marcas = sub('\]',')', marcas)

        combustiveis = str(filtro.getCombustivel())
        combustiveis = sub('\[','(', combustiveis)
        combustiveis = sub('\]',')', combustiveis)

        Combustivel = '' if (filtro.getCombustivel() == 'NULL' or combustiveis == "('')") else f"AND Combustivel IN {combustiveis}"
        Marca = '' if (marca == '' or marcas == "('')") else f"AND Marca IN {marcas}"
        Modelo = '' if (modelo == '') else f"AND Modelo = '{modelo}'"

        query = """
            SELECT * FROM carvago.Carros
                WHERE
                    Ano >= %s AND Ano <= %s AND Preco >= %s AND Preco <= %s AND Quilometros >= %s AND Quilometros <= %s %s %s %s
                    %s
                    LIMIT 10 OFFSET %s;
        """%(filtro.getAnoMinimo(), filtro.getAnoMaximo(), filtro.getPrecoMinimo(), filtro.getPrecoMaximo(), filtro.getKMMinimo(), filtro.getKMMaximo(), Combustivel, Marca, Modelo, ordemBY, str((num_pag-1)*10) )

        cursor.execute(query)

        carros = []
        for r in cursor:
            id = int(r[0])
            anunciante = r[1]
            marca = r[2]
            modelo = r[3]
            versao = r[4]
            combustivel = r[5]
            mes_registo = r[6]
            ano = int(r[7])
            quilometros = int(r[8])
            cilindrada = int(r[9])
            potencia = int(r[10])
            cor = r[11]
            tipo_cor = r[12]
            tipo_caixa = r[13]
            num_portas = int(r[14])
            origem = r[15]
            condicao = r[16]
            preco = float(r[17])
            link_foto = r[18]
            titulo = r[19]
            link_anuncio = r[20]
            id_anuncio = int(r[21])
            fonte = r[22]

            fav = self.isCarroInFavoriteUser(id_user, id)

            carro = Carro( anunciante, marca, modelo, versao, combustivel, mes_registo, ano, quilometros, cilindrada, potencia, cor, 
                           tipo_cor, tipo_caixa, num_portas, origem, condicao, preco, link_foto, titulo, link_anuncio, id_anuncio, fonte, ID=id, Favorito=fav)
            
            carros.append(carro)

        return carros
    
    def getNumPagesCarrosAvailable(self, marca : str, modelo : str, filtro : FiltrosNotificacoes, num_pag) -> list:
        _, cursor = connectToDB()
        
        from re import sub
        marcas = str(marca)
        marcas = sub('\[','(', marcas)
        marcas = sub('\]',')', marcas)

        combustiveis = str(filtro.getCombustivel())
        combustiveis = sub('\[','(', combustiveis)
        combustiveis = sub('\]',')', combustiveis)

        Combustivel = '' if (filtro.getCombustivel() == 'NULL' or combustiveis == "('')") else f"AND Combustivel IN {combustiveis}"
        Marca = '' if (marca == '' or marcas == "('')") else f"AND Marca IN {marcas}"
        Modelo = '' if (modelo == '') else f"AND Modelo = '{modelo}'"

        query = """
            SELECT count(*) FROM carvago.Carros
                WHERE
                    Ano >= %s AND Ano <= %s AND Preco >= %s AND Preco <= %s AND Quilometros >= %s AND Quilometros <= %s %s %s %s;
        """%(filtro.getAnoMinimo(), filtro.getAnoMaximo(), filtro.getPrecoMinimo(), filtro.getPrecoMaximo(), filtro.getKMMinimo(), filtro.getKMMaximo(), Combustivel, Marca, Modelo )

        cursor.execute(query)
        r = cursor.fetchone()

        import math
        return math.ceil(int(r[0]) / 10 )

    def getImagensCarros(self) -> list:
        _, cursor = connectToDB()

        query = """
            SELECT Link_foto, Titulo, Preco FROM carvago.Carros;
        """

        cursor.execute(query)
        
        imagens_links = []
        from re import split
        for r in cursor:
            links = r[0]
            links = split(' ', links)

            temp = {}
            temp['link_foto'] = links[0].strip()
            temp['titulo'] = r[1]
            temp['preco'] = float(r[2])
            imagens_links.append(temp)
        
        return imagens_links

