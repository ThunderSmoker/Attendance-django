# Create your models here.
from django.db import models
 
class Student(models.Model):
    date = models.CharField(max_length = 200)
    batch=models.CharField(max_length=4)
    prn=models.IntegerField(max_length=20)
    sub=models.CharField(max_length=30)
    present=models.BooleanField(default=False)

class Batch(models.Model):
    batch=models.CharField(max_length=4)
    prn=models.IntegerField(max_length=20)

#mongodb://localhost:27017