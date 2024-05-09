import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="pythontesting"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for i in mycursor:
    print(i)