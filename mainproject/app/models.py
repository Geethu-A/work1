from django.db import models

# Create your models here.
# class Product(models.Model):
#     name=models.CharField(max_length=50)
#     email=models.CharField(max_length=50)
#     phone=models.IntegerField()
#     date=models.IntegerField()
#     time=models.IntegerField()
class Appointmentsss(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    date=models.DateField()
    time=models.CharField(max_length=10)
    message=models.CharField(max_length=50)