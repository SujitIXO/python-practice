import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "pythontesting",
)

mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE customers (id INT NOT NULL PRIMARY KEY, name VARCHAR(50), address VARCHAR(30), age INT, phoneNo VARCHAR(15) )')

mycursor.execute("INSERT INTO customers (id, name, address, age, phoneNo) VALUES(12, 'srk', 'bbsr', 24, 9876457809)")

mydb.commit()

print(mycursor.rowcount, "was inserted.")