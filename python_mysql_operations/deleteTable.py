import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "pythontesting"
)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE customers")
print("table deleted successfully")