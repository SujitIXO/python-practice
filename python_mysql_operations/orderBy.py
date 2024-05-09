import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "pythontesting"
)

mycursor = mydb.cursor()

sql = "delete from students where address = 'Ocean blvd 2'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "deleted")

