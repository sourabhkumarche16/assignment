import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="sourabhche16",
  password="Ibadlyneedthisjob",
  database="mydb1"
)

cur = mydb.cursor()

s = "SELECT \
  CUSTOMER.FIRST_NAME, \
  FROM CUSTOMER \
  INNER JOIN ADDRESS ON CUSTOMER.ADDRESS_ID = ADDRESS.ADDRESS_ID"

cur.execute(s)

res = cur.fetchall()

for x in res:
  print(x)