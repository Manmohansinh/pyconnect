import mysql.connector as SQLC
DataBase = SQLC.connect(
    host="localhost",
    user="root",
    password="manmohan65",
    port="3306",
    database="Hospital"
)
Cursor = DataBase.cursor()

TableName = "CREATE TABLE patient(cust_ID int(11) NOT NULL,Name varchar(255) NOT NULL,Open_date date NOT NULL,Consult_dt date NOT NULL,VAC_ID char(5) NOT NULL,Dr_Name varchar(45) DEFAULT NULL,State char(5) DEFAULT NULL,Country char(5) NOT NULL,DOB date DEFAULT NULL,Active char(3) NOT NULL,PRIMARY KEY (`cust_ID`));"

Cursor.execute(TableName)
print("patient Table is Created in the Database")
