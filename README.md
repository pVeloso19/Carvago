# Carvago

## Aplicação **- Fullstack -** para a monitorização de carros à venda. 
</br>

> Esta aplicação pretende possibilitar aos seus utilizadores o acompanhamento dos carros existentes para vendas em vários websites, numa única página. Assim, realiza-se um aglomerado da oferta existente e apresenta-se essa informação aos utilizadores.
>
> Para além disto, será possível especificar determinadas condições em que a entrada de um novo veículo, que as cumpra, notificará o utilizador.
>
> Com a atualização constante dos carros existentes nas várias fontes, será possivel ficar por dentro das novidades. **Assim, a utilização do Carvago permite aos seus utilizadores o acompanhamento constante do mercado, não perdendo nenhuma novidade, tornando mais fácil encontrar o melhor negócio para os seus veículos de sonho.**
</br>

## Instalação

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

## Resultado Final

### Página inicial (Sem Login efetuado)
<img src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626682865340456/Captura_de_Ecra_8.png?width=971&height=546">
<img src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626522122825838/Screenshot_20220729_181819_com.huawei.browser.jpg?width=255&height=545" height="400px">

### Login/Criar conta
<picture>
  <img alt="Login PC" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626683221848185/Captura_de_Ecra_9.png?width=971&height=546" style="max-height: 232px;">
</picture>

<img alt="Login Tele" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626521887952906/Screenshot_20220729_181822_com.huawei.browser.jpg?width=255&height=545" style="max-height: 232px;">

<picture>
  <img alt="Criar Conta PC" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626683762921482/Captura_de_Ecra_10.png?width=971&height=546" style="max-height: 232px;">
</picture>

<picture>
  <img alt="Criar Conta Tele" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626521686610032/Screenshot_20220729_181827_com.huawei.browser.jpg?width=255&height=545" style="max-width:30px; max-height: 32px;">
</picture>

### Home Page
<picture>
  <img alt="HomePage PC" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626682093584494/Captura_de_Ecra_11.png?width=971&height=546" style="max-height: 232px;" >
  <img alt="HomePage Tele" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626521451733133/Screenshot_20220729_181908_com.huawei.browser.jpg?width=255&height=545" style="max-height: 232px;" >
</picture>

### Todos os carros
<picture>
  <img alt="TodosCarros PC" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626682437500938/Captura_de_Ecra_12.png?width=971&height=546" style="max-height: 231px;" >
  <img alt="TodosCarros Tele" src="https://media.discordapp.net/attachments/1002574979252105312/1002628823835213834/Screenshot_20220729_182849_com.huawei.browser.jpg?width=255&height=545" style="max-height: 231px;" >
</picture>

### Adicionar Interesses
<picture>
  <img alt="ADDInteresse PC" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626684262035556/Captura_de_Ecra_13.png?width=971&height=546" style="max-height: 232px;" >
  <img alt="ADDInteresse Tele" src="https://cdn.discordapp.com/attachments/1002574979252105312/1002626521183305789/Screenshot_20220729_181927_com.huawei.browser.jpg?width=255&height=545" style="max-height: 231px;" >
</picture>

### Favoritos/Novos Carros (Sem Resultados)
<picture>
  <img alt="Sem Resultados PC" src="https://media.discordapp.net/attachments/1002574979252105312/1002629604240007238/Captura_de_Ecra_14.png?width=971&height=546" style="max-height: 232px;" >
  <img alt="Sem Resultados Tele" src="https://media.discordapp.net/attachments/1002574979252105312/1002629520563650650/Screenshot_20220729_183140_com.huawei.browser.jpg?width=255&height=545" style="max-height: 231px;" >
</picture>
