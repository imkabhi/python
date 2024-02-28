import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'abc',
    password = 'password'
)

mycursor = mydb.cursor()
mycursor.execute('INSERT INTO test1.test_table values(3424, "abhi", 567, 987.09, "ram") ')
mycursor.execute('INSERT INTO test1.test_table values(3424, "abhi", 567, 987.09, "ram") ')
mycursor.execute('INSERT INTO test1.test_table values(3424, "abhi", 567, 987.09, "ram") ')
mycursor.execute('INSERT INTO test1.test_table values(3424, "abhi", 567, 987.09, "ram") ')
mycursor.execute('INSERT INTO test1.test_table values(3424, "abhi", 567, 987.09, "ram") ')
mycursor.execute('INSERT INTO test1.test_table values(3424, "abhi", 567, 987.09, "ram") ')
mycursor.execute('INSERT INTO test1.test_table values(3424, "abhi", 567, 987.09, "ram") ')
mycursor.execute('INSERT INTO test1.test_table values(3424, "abhi", 567, 987.09, "ram") ')
mycursor.execute('INSERT INTO test1.test_table values(3424, "abhi", 567, 987.09, "ram") ')

mydb.commit()
mydb.close()