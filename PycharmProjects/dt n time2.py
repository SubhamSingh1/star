import datetime
print("Current Date n time ")
print(datetime.datetime.now())
print()

print("creating date object")
print(datetime.datetime(2018,12,10))
print()
print("creating date object #2")
print(datetime.datetime(2018,12,10,14,15,10))
print()

from datetime import datetime as dt
print("Comparing time b/w  8 am to 4 pm")
if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,16):
    print("Working hours")
else:
    print("Fun hours")
print()

import calendar
print("printing calendar of month dec 19")
cal=calendar.month(2019,12)
print(cal)
print()

print("printing the calendar of whole year")
calendar.prcal(2019)