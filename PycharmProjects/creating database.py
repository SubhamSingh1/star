import mysql.connector
myconn=mysql.connector.connect(host="localhost",user="root",password="root")
cur= myconn.cursor()
try:
    cur.execute("create database pythonDB")
    dbs=cur.execute("show databases")
except:
    myconn.rollback()
for x in cur:
    print(x)
myconn.close()


