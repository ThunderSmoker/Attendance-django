# Create your models here.
from django.db import models
 
class Student(models.Model):
    date = models.CharField(max_length = 200)
    batch=models.CharField(max_length=4)
    prn=models.IntegerField(max_length=20)
    present=models.BooleanField(default=False)


