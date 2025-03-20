from flask_sqlalchemy import SQLAlchemy
import pymysql

connection = pymysql.connect(host='localhost', user='root', password='password')
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS dongalleto")
cursor.close()
connection.close()

bd = SQLAlchemy()