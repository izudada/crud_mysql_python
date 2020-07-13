import mysql.connector

config = {
    'user' : 'root',
    'password' : '',
    'host' : 'localhost',
    'database' : 'crud'
}

db = mysql.connector.connect(**config)

cursor = db.cursor()