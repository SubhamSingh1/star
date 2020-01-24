import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", password="root", database="pythonDB")
cur = myconn.cursor()
sql = "insert into Employee(name,id,salary,dept_id,branch_name)values(%s,%s,%s,%s,%s)"
val = ("MikeS", 251, 28000, 202, "Guyana")
try:
    huh= cur.execute(sql, val)
    myconn.commit()
    print(cur.rowcount,"record inserted ! id:",cur.lastrowid)
except:
    myconn.rollback()

