from django.db import models

class Employee(models.Model):
    eid = models.CharField(max_length=20 ,default="")
    eemail = models.EmailField(default='')
    ename = models.CharField(max_length=100,default='')
    econtact = models.CharField(max_length=20, default='')