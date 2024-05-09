import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "pythontesting"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM students")

result = mycursor.fetchone()

print(result)