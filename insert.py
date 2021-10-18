import mysql.connector as SQLC
DataBase = SQLC.connect(
    host="localhost",
    user="root",
    password="manmohan65",
    port="3306",
    database="Hospital"
)

Cursor = DataBase.cursor()

sql = "INSERT INTO patient (cust_ID,Name,Open_date,Consult_dt,VAC_ID,Dr_Name,State,Country,DOB,Active) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

val = [(1, 'Alex', 20150115, 20150121, 'MVX', 'Paul', 'SA', 'USA', 19980204, 'Yes'),
       (2, 'John', 20150906, 20150911, 'MCV', 'Paul', 'CA', 'USA', 19990606, 'Yes'),
       (3, 'Sumith', 20161123, 20161129, 'MVX', 'Reddy', 'KA', 'IND', 19980816, 'Yes'),
       (4, 'Joma', 20170809, 20170815, 'MVX', 'Chuck', 'VIC', 'AU', 19970101, 'No'),
       (5, 'Mathew', 20141217, 20141225, 'MCV', 'Bill', 'WAS', 'PHIL', 19980223, 'Yes'),
       (6, 'Matt', 20180529, 20180604, 'MXV', 'Paul', 'NY', 'USA', 20000812,'Yes'),
       (7, 'Atherv', 20190606, 20190615, 'MXV', 'Reddy', 'MH', 'IND', 20000204, 'Yes'),
       (8, 'Robin', 20170809, 20170817, 'MCV', 'Chuck', 'VIC', 'AU', 19961210,'No'),
       (9, 'Gaurav', 20200607, 20200614, 'MVX', 'Reddy', 'MH', 'IND', 19990103, 'Yes'),
       (10, 'Jacob', 20180725, 20180730, 'MXV', 'Andrew', 'LI', 'UK', 19990707, 'No'),
       (11, 'Marshal', 20170117, 20200305, 'MCX', 'Andrew', 'LI', 'UK', 19980814, 'Yes'),
       (12, 'Sergio', 20160912, 20160918, 'MCV', 'Paul', 'TX', 'USA',19970523, 'No')]

Cursor.executemany(sql, val)
DataBase.commit()
print("Data inserted successfully")