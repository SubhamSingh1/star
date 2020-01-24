import mysql.connector

myconn = mysql.connector.connect(host="localhost", user="root", password="root", database="pythonDB")
cur = myconn.cursor()
sql = "insert into Employee(name,id,salary,dept_id,branch_name)values(%s,%s,%s,%s,%s)"
val = [("john", 10, 25000.00, 201, "Newyork"),("david",103,250000.00,202,"port of spain"),("Nck",104,90000,201,"Newyork")]
try:
    cur.executemany(sql,val)
    myconn.commit()
    print(cur.rowcount,"records inserted")
except:
    myconn.rollback()
myconn.close()