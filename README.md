# Carvago

## Aplicação **- Fullstack -** para a monitorização de carros à venda. 
</br>

> Esta aplicação pretende possibilitar aos seus utilizadores o acompanhamento dos carros existentes para vendas em vários websites, numa única página. Assim, realiza-se um aglomerado da oferta existente e apresenta-se essa informação aos utilizadores.
>
> Para além disto, será possível especificar determinadas condições em que a entrada de um novo veículo, que as cumpra, notificará o utilizador.
>
> Com a atualização constante dos carros existentes nas várias fontes, será possivel ficar por dentro das novidades. **Assim, a utilização do Carvago permite aos seus utilizadores o acompanhamento constante do mercado, não perdendo nenhuma novidade, tornando mais fácil encontrar o melhor negócio para os seus veículos de sonho.**
</br>

## Instalação (Sem Docker)

> Para utilizar a aplicação deve ter instalado:
> - Flask (pip install Flask)
> - Requests (pip install requests)
> - Flask-Cors (pip install Flask-Cors)
> - Pywebpush (pip install pywebpush)
> - Jsons (pip install jsons)
> - Regex (pip install regex)
> - Mysql-connector-python (pip install mysql-connector-python)
> - BeautifulSoup (pip install beautifulsoup4)
> - SSL (pip install ssl)
> - O SGBD mySQL instalado e configurado. (para configurar a base de dados deve-se correr o código SQL disponibilizado [aqui](https://github.com/pVeloso19/Carvago/blob/main/Site/BaseDados/Creat.sql) responsável por criar o esquema da BD e as respetiveis tabelas. Por fim, tem de se colocar os dados corretos no [ficheiro de configuração](https://github.com/pVeloso19/Carvago/blob/main/Site/BaseDados/DBConexao.py))
>
> Para executar a Backend basta correr o ficheiro main.py (*a execução deve ser realizada dento da pasta Site, devido às dependencias com os restantes ficheiros*), que executará a aplicação **flask** desenvolvida, bem como numa thread diferente a componente que atualiza (de 2 em 2 horas) os dados da base de dados.
>
> Por fim, basta utilizar o browser para aceder à interface criada, via HTTP.
</br>

## Instalação (Com Docker)

> Para realizar à instalação do programa com o docker é necessário:
>
> - Ter o docker instalado e configurado
> - O SGBD mySQL instalado e configurado. (para configurar a base de dados deve-se correr o código SQL disponibilizado [aqui](https://github.com/pVeloso19/Carvago/blob/main/Site/BaseDados/Creat.sql) responsável por criar o esquema da BD e as respetiveis tabelas. Também é disponibilizado um dockerfile para criar o container docker com a base de dados ([aqui]())
>
> Para executar o container docker:
>
> - 1º - Criar a imagem do container -> docker build -t <nome_imagem> <path_do_dockerfile>
> - 2º - Executaro container -> docker run --name="<nome_do_container>" -p5000:5000 -d <nome_imagem_definido_no_passo_anterior>
> - Existe algumas variaveis que se pode defenir durante a execução do container:
>   - DATABASE_IP : Endereço IP da máquina em que a base de dados se encontra
>   - MYSQL_DATABASE : Nome da base de dados criada
>   - MYSQL_ROOT_PASSWORD : Palavra passe do utilizador root, para aceder à base de dados

## Resultado Final

### Página inicial (Sem Login efetuado)
<p display="flex" align-items="stretch">
<img src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626682865340456/Captura_de_Ecra_8.png?width=971&height=546" width="70%">

<img src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626522122825838/Screenshot_20220729_181819_com.huawei.browser.jpg?width=255&height=545" height="400px">
<p>

### Login/Criar conta
<p display="flex" align-items="stretch">
<img alt="Login PC" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626683221848185/Captura_de_Ecra_9.png?width=971&height=546" width="70%">

<img alt="Login Tele" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626521887952906/Screenshot_20220729_181822_com.huawei.browser.jpg?width=255&height=545" height="400px">

<img alt="Criar Conta PC" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626683762921482/Captura_de_Ecra_10.png?width=971&height=546" width="70%">

<img alt="Criar Conta Tele" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626521686610032/Screenshot_20220729_181827_com.huawei.browser.jpg?width=255&height=545" height="400px">
<p>

### Home Page
<p display="flex" align-items="stretch">
<img alt="HomePage PC" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626682093584494/Captura_de_Ecra_11.png?width=971&height=546"  width="70%">

<img alt="HomePage Tele" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626521451733133/Screenshot_20220729_181908_com.huawei.browser.jpg?width=255&height=545" height="400px" >
<p>

### Todos os carros
<p display="flex" align-items="stretch">
<img alt="TodosCarros PC" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626682437500938/Captura_de_Ecra_12.png?width=971&height=546"  width="70%">

<img alt="TodosCarros Tele" src="https://media.discordapp.net/attachments/1002574979252105312/1002628823835213834/Screenshot_20220729_182849_com.huawei.browser.jpg?width=255&height=545" height="400px">
<p>

### Adicionar Interesses
<p display="flex" align-items="stretch">
<img alt="ADDInteresse PC" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626684262035556/Captura_de_Ecra_13.png?width=971&height=546"  width="70%">

<img alt="ADDInteresse Tele" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626521183305789/Screenshot_20220729_181927_com.huawei.browser.jpg?width=255&height=545" height="400px" >
<p>

### Favoritos/Novos Carros (Sem Resultados)
<p display="flex" align-items="stretch">
<img alt="Sem Resultados PC" src="https://media.discordapp.net/attachments/1002574979252105312/1002629604240007238/Captura_de_Ecra_14.png?width=971&height=546"  width="70%">

<img alt="Sem Resultados Tele" src="https://media.discordapp.net/attachments/1002574979252105312/1002629520563650650/Screenshot_20220729_183140_com.huawei.browser.jpg?width=255&height=545" height="400px" >
<p>
