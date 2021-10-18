import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password123',
    port='3306',
    database='schema'
)

mycursor = mydb.cursor()

mycursor.execute()
