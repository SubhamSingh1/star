import mysql.connector
myconn=mysql.connector.connect(host="localhost",user="root",password="root",database="star1")
print(myconn)
cur= myconn.cursor()
print(cur) 