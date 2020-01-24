import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", password="root", database="pythonDB")
cur = myconn.cursor()
sql = "insert into Employee(name,id,salary,dept_id,branch_name)values(%s,%s,%s,%s,%s)"
val = ("john", 110, 25000.00, 201, "Newyork")
try:
    huh= cur.execute(sql, val)
    myconn.commit()
except:
    myconn.rollback()
print(cur.rowcount, ("record inserted"))
myconn.close()
