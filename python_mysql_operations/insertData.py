import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="pythontesting"
)

mycursor = mydb.cursor()

sql = "INSERT INTO students (name, address) VALUES (%s, %s)"

val = [
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")