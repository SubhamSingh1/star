import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", password="root", database="pythonDB")
cur = myconn.cursor()
try:
    cur.execute("Select * from employee")
    result = cur.fetchall()

    for x in result:
        print(x)
except:
    myconn.rollback()
myconn.close()
