import mysql.connector as SQLC
DataBase = SQLC.connect(
    host="localhost",
    user="root",
    password="password123",
    port="3306",
    database="Hospital"
)

Cursor = DataBase.cursor ( )
sql = "SELECT * FROM patient WHERE Country = 'IND'"
Cursor.execute(sql)
myresult =Cursor.fetchall ( )
for x in myresult :
  print(x)
