import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin"
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)