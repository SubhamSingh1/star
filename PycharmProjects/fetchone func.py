import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", password="root", database="pythonDB")
cur = myconn.cursor()
try:
    cur.execute("select name,id,salary from employee")
    result=cur.fetchone()
    print(result)
except:
    myconn.rollback()
myconn.close()