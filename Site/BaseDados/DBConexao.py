import mysql.connector

DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASS = 'Pedro1234'
DB_NAME = 'carvago'

def connectToDB():
    connection = mysql.connector.connect(
        host= DB_HOST,
        user= DB_USER,
        password= DB_PASS,
        database= DB_NAME
    )

    cursor = connection.cursor()
    return (connection, cursor)



