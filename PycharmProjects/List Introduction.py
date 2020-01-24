emp=["John",102,"Usa"]
dep1=["CS",10]
dep2=["IT",11]
hod_cs=[10,"Mr.Holding"]
hod_it=[11,"Mr. bewon"]
print("\nEmployee Data")
print("Name:%s,ID:%d,country:%s"%(emp[0],emp[1],emp[2]),)
print()
print("Department details")
print("Department 1:\nname:%s,ID:%d\nDepartment 2:\nName:%s,ID:%d"%(dep1[0],dep1[1],dep2[0],dep2[1]))
print()
print("HOD details")
print("CS HOD name:%s,ID:%d"%(hod_cs[1],hod_cs[0]))
print("IT HOD name:%s,ID:%d"%(hod_it[1],hod_it[0]))
print()
print(type(emp),type(dep1),type(dep2),type(hod_cs),type(hod_it))
