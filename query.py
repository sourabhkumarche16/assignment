import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sourabhche16",
  password="Ibadlyneedthisjob",
  database="mydb1"
)

cur = mydb.cursor()

s = "SELECT * FROM address WHERE address ='Park Lane 38'"

cur.execute(s)

res = cur.fetchall()

for x in res:
  print(x)