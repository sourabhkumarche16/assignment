import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sourabhche16",
  password="Ibadlyneedthisjob",
  database="mydb1"
)

cur = mydb.cursor()

s = "SELECT COUNT(LANGUAGE_ID) FROM LANGUAGE;"

cur.execute(s)

res = cur.fetchall()

for x in res:
  print(x)