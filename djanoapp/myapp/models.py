from django.db import models
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=10)
    econtact = models.CharField(max_length=20)
    class Meta:
        db_table = 'employee'


# Create your models here.
