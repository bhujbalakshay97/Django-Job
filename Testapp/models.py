from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    enname=models.CharField(max_length=87)
    esal=models.FloatField()
    eaddr=models.TextField()
    email=models.EmailField()
