from django.db import models

# Create your models here.
class College(models.Model):
    dept=models.CharField(max_length=20)
    def __str__(self):
        return self.dept
class Teacher(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    dept=models.ForeignKey(College,on_delete=models.CASCADE)