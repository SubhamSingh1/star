import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", password="root", database="pythonDB")
cur = myconn.cursor()
try:
    cur.execute("select name,id,salary from employee order by name")
    result=cur.fetchall()
    print("name id salary")
    for row in result:
        print("%s %d %d"%(row[0],row[1],row[2]))

except:
    myconn.rollback()
myconn.close()