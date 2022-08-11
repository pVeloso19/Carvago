FROM ubuntu
RUN mkdir /app
COPY /Site /app
WORKDIR /app

ENV DATABASE_IP 127.0.0.1
ENV MYSQL_DATABASE carvago
ENV MYSQL_ROOT_PASSWORD Pedro1234

RUN apt-get update
RUN apt-get install python3-pip -y

RUN pip3 install Flask
RUN pip3 install requests
RUN pip3 install Flask-Cors
RUN pip3 install pywebpush
RUN pip3 install jsons
RUN pip3 install regex
RUN pip3 install mysql-connector-python
RUN pip3 install beautifulsoup4

EXPOSE 5000

CMD sed -i "s/DB_HOST = '127.0.0.1'/DB_HOST = '${DATABASE_IP}'/" ./BaseDados/DBConexao.py && sed -i "s/DB_PASS = 'Pedro1234'/DB_PASS = '${MYSQL_ROOT_PASSWORD}'/" ./BaseDados/DBConexao.py && sed -i "s/DB_NAME = 'carvago'/DB_NAME = '${MYSQL_DATABASE}'/" ./BaseDados/DBConexao.py && python3 main.py