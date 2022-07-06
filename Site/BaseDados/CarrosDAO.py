
from BaseDados.DBConexao import connectToDB
from Carros.Carro import Carro

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

    def getAllCarrosByMarcaANDModelo(self, marca : str, modelo : str) -> list:
        _, cursor = connectToDB()

        query = """
            select * from carvago.Carros
                where Marca = '%s' and Modelo = '%s';
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

            carro = Carro( anunciante, marca, modelo, versao, combustivel, mes_registo, ano, quilometros, cilindrada, potencia, cor, 
                           tipo_cor, tipo_caixa, num_portas, origem, condicao, preco, link_foto, titulo, link_anuncio, id_anuncio, fonte, ID=id)
            
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
                WHERE idCarros in %s;
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

            carro = Carro( anunciante, marca, modelo, versao, combustivel, mes_registo, ano, quilometros, cilindrada, potencia, cor, 
                           tipo_cor, tipo_caixa, num_portas, origem, condicao, preco, link_foto, titulo, link_anuncio, id_anuncio, fonte, ID=id)
            
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
                WHERE idCarros in %s;
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
                           tipo_cor, tipo_caixa, num_portas, origem, condicao, preco, link_foto, titulo, link_anuncio, id_anuncio, fonte, ID=id)
            
            carros.append(carro)

        return carros

    def marcaCarrosComoVistos(delf, id_user : int):
        connection, cursor = connectToDB()

        query = """
            DELETE FROM carvago.Carros_Nao_Vistos
	            WHERE User_idUser = %s;
        """%( str(id_user) )

        cursor.execute(query)
        connection.commit()



