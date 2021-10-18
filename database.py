import mysql.connector as SQLC
DataBase = SQLC.connect(
    host="localhost",
    user="root",
    password="manmohan65",
    port="3306"
)
# Cursor to the database
Cursor = DataBase.cursor()

Cursor.execute("CREATE DATABASE Hospital")
print("Hospital Data base is created")
