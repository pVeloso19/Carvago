from bs4 import BeautifulSoup

import ssl
import requests

class StandVirtualGather:

    def __init__(self):
        pass

    def getDados(self, marca = 'ford', modelo = 'focus') -> dict:
        
        ssl._create_default_https_context = ssl._create_unverified_context
        result = requests.request("GET", f"https://www.standvirtual.com/carros/{marca}/{modelo}")
        html_doc = result.text
        soup = BeautifulSoup(html_doc, 'html.parser')

        temp1 = soup.find_all('article')
        temp2 = {}
        for article in temp1:
            if('data-testid="listing-ad"' in str(article)):
                temp2[ str(article.h2.a['href']) ] = ''

        paginas = soup.find_all("ul", "pagination-list")[0]
        paginas = paginas.find_all("li")
        max_pag = 1
        for pagina in paginas:
            try:
                num_pag = pagina.a.span.contents[0].strip()
                max_pag = int(num_pag)
            except:
                pass

        i = 2
        while(i <= max_pag):
            result = requests.request("GET", f"https://www.standvirtual.com/carros/{marca}/{modelo}?page={i}")
            html_doc = result.text
            soup = BeautifulSoup(html_doc, 'html.parser')

            temp1 = soup.find_all('article')
            for article in temp1:
                if('data-testid="listing-ad"' in str(article)):
                    temp2[ str(article.h2.a['href']) ] = ''
            
            i += 1

        temp3 = []
        for link, _ in temp2.items():

            result = requests.request("GET", link)
            html_doc = result.text
            soup = BeautifulSoup(html_doc, 'html.parser')

            temp1 = soup.find_all('li')
            
            res = {}

            id = soup.find_all(id="ad_id")[0].contents[0].strip()
            res['ID'] = id

            for li in temp1:
                
                if('class="offer-params__item"' in str(li)):
                    valor = li.div.a
                    if(valor is not None):
                        valor = valor.contents[0].strip()
                    else:
                        valor = li.div.contents[0].strip()
                    
                    chave = li.span.contents[0]

                    res[chave] = valor

            temp3.append(res)

        return temp3


#file1 = open("temp.html", "w", encoding='utf-8') 
#file1.write(html_doc)
#file1.close()