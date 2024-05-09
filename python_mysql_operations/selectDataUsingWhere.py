import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "pythontesting"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM students WHERE name = 'Peter'")

res = mycursor.fetchall()

print(res)