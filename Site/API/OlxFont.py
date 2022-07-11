import re
from bs4 import BeautifulSoup

import ssl
import requests

from Carros.Carro import Carro
from BaseDados.CarrosDAO import CarrosDAO

class OLXGather:

    def __init__(self):
        pass

    def __getDados(self, marca = 'ford', modelo = 'focus') -> (dict and list):
        
        ssl._create_default_https_context = ssl._create_unverified_context
        result = requests.request("GET", f"https://www.olx.pt/carros-motos-e-barcos/carros/{marca}/?search%5Bfilter_enum_modelo%5D%5B0%5D={modelo}")
        html_doc = result.text

        soup = BeautifulSoup(html_doc, 'html.parser')

        temp1 = soup.find_all('td', 'offer')
        temp2 = {}
        
        for offer in temp1:
            temp2[ str(offer.div.table.tbody.tr.td.a['href']) ] = ''

        paginas = soup.find_all("span", "item fleft")
        max_pag = 1
        for pagina in paginas:
            try:
                num_pag = pagina.span.span.contents[0].strip()
                max_pag = int(num_pag)
            except:
                num_pag = pagina.a.span.contents[0].strip()
                max_pag = int(num_pag)

        i = 2
        while(i <= max_pag):
            result = requests.request("GET", f"https://www.olx.pt/carros-motos-e-barcos/carros/{marca}/?search%5Bfilter_enum_modelo%5D%5B0%5D={modelo}&page={i}")
            html_doc = result.text
            soup = BeautifulSoup(html_doc, 'html.parser')

            temp1 = soup.find_all('td', 'offer  ')
            for offer in temp1:
                temp2[ str(offer.div.table.tbody.tr.td.a['href']) ] = ''
            
            i += 1


        temp3 = []
        for link, _ in temp2.items():
            
            if('standvirtual' not in link):
                result = requests.request("GET", link)
                html_doc = result.text
                soup = BeautifulSoup(html_doc, 'html.parser')
                
                res = {}

                res['ID'] = soup.find_all('span','css-9xy3gn-Text eu5v0x0')[0].contents[2].strip()

                res['PRECO'] = soup.find_all('h3','css-okktvh-Text eu5v0x0')[0].contents[0].strip().replace(".","")
                res['Link_foto'] = []
                res['Titulo'] = soup.find_all('h1','css-r9zjja-Text eu5v0x0')[0].contents[0].strip()
                res['Link_anuncio'] = link

                temp1 = soup.find_all('div','swiper-zoom-container')
                for img in temp1:
                    src = str(img.img)
                    src = re.search('src="([^"]*)"', src)
                    res['Link_foto'].append(src.groups(1)[0])

                res['Anunciante'] = ''
                res['Marca'] = ''
                res['Versão'] = ''
                res['Combustível'] = ''
                res['Mês de Registo'] = ''
                res['Ano'] = 0 
                res['Cor'] = ''
                res['Tipo de cor'] = ''
                res['Tipo de Caixa'] = ''            
                res['Número de Mudanças'] = '' 
                res['Nº de portas'] = 0
                res['Origem'] = ''
                res['Condição'] = ''
                res['Quilómetros'] = '-1 km'
                res['Cilindrada'] = '-1 cm3'
                res['Potência'] = '-1 cv'

                temp1 = soup.find_all('li', 'css-ox1ptj')
                for li in temp1:
                    try:
                        valor = li.p.span.contents[0].strip()
                        res['Anunciante'] = valor
                    except:
                        valor = li.p.contents[0].strip()
                        valor = re.split(':', valor)
                        chave = valor[0].strip()
                        valor = valor[1].strip()
                        res[chave] = valor

                temp3.append(res)


        carros = {}
        lista_carros = []
        for c in temp3:
            
            quilometros = int(re.sub('[a-zA-Z].*', '', c['Quilómetros']).strip().replace(" ","").replace(".",""))
            cilindrada = int(re.sub('[a-zA-Z].*', '', c['Cilindrada']).strip().replace(" ",""))
            potencia = int(re.sub('[a-zA-Z].*', '', c['Potência']).strip().replace(" ",""))

            link_foto = ''
            i = 0
            while (i < len(c['Link_foto']) ):
                link_foto += c['Link_foto'][i]
                i+=1
                if(i < (len(c['Link_foto'])) ):
                    link_foto += ' '

            carro = Carro( c['Anunciante'], c['Marca'], c['Modelo'], c['Versão'], c['Combustível'], c['Mês de Registo'], 
                           int(c['Ano']), quilometros, cilindrada, potencia, c['Cor'], c['Tipo de cor'], c['Tipo de Caixa'],
                           int(c['Nº de portas']), c['Origem'], c['Condição'], float(c['PRECO']), link_foto, c['Titulo'],
                           c['Link_anuncio'], int(c['ID']), 'olx')

            carros[carro.getIDAnuncio()] = carro
            lista_carros.append(carro)
        
        return (carros, lista_carros)
 
    def getDados(self, marcas_modelos = []) -> (list and list):

        carrosDAO = CarrosDAO.instance()

        lista_carros_novos = []
        lista_id_carros_vendidos = []
        
        for marca, modelo in marcas_modelos:
            dados_dict, dados_list = self.__getDados(marca=marca, modelo=modelo)

            lista_ids_existentes = carrosDAO.getAllIDAnuncioCarrosByMarcaANDModeloANDFonte(marca, modelo, 'olx')

            # verifica novos carros
            for carro in dados_list:
                id = carro.getIDAnuncio()
                if(id not in lista_ids_existentes):

                    #Insere o carro que não existia na Base de Dados
                    id_carro = carrosDAO.insertCarro(carro)

                    #Define o ID do carro para o id que se inseriu na Base de Dados
                    carro.setID(id_carro)
                    
                    #Adiciona o carro à lista para notificar
                    lista_carros_novos.append(carro)

                    #Povoar a tabela de Carros_Nao_Vistos
                    carrosDAO.insertCarrosNaoVisto(id_carro, carro)

            # verifica se existem carros que foram vendidos
            for id in lista_ids_existentes:
                if(id not in dados_dict):
                    carrosDAO.deleteCarroByIDAnuncioANDFonte(id, 'olx')
                    lista_id_carros_vendidos.append(id)

            #Atualiza os dados dos carros na base de dados
            for carro in dados_list:
                carrosDAO.updateCarroByIDAnuncioANDFonte(carro)

        return (lista_carros_novos, lista_id_carros_vendidos)
