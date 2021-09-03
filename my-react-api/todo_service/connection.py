import mysql.connector

cnx = mysql.connector.connect(user='root', password='Aa@-138205175', host='127.0.0.1')

mycursor = cnx.cursor()
mycursor.execute("CREATE DATABASE mydatabase")