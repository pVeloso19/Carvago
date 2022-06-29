
from BaseDados.DBConexao import connectToDB

class CarrosDAO:
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def insertCarros(self, listaCarros : list) -> bool:
        for carro in listaCarros:
            
            connection, cursor = connectToDB()

            query = """
                INSERT INTO carvago.Carros
                    VALUES
                        (%s, '%s', '%s', '%s', '%s', '%s', '%s', %s, %s, %s, %s, '%s', '%s', '%s', %s, '%s', '%s', %s, '%s', '%s', '%s')
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
                        Link_anuncio = VALUES(Link_anuncio);
            """%(
                    str(carro.getID()), 
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
                    carro.getLink_anuncio()
                )


            print(query)
            print('\n')
            print('\n')
            print('\n')
            print('\n')

            cursor.execute(query)
            connection.commit()
        
        return True