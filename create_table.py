import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE if NOT exists test1.test_table(c1 INT, c2 VARCHAR(50), c3 INT, c4 FLOAT, c5 VARCHAR(40))")
mydb.close()
