from django.db import models

# Create your models here.

class student_info(models.Model):
    Name = models.CharField(max_length=100)
    F_name = models.CharField(max_length=100)
    I_name = models.CharField(max_length=500)
    Batch = models.TextField()

class student_marks(models.Model):
     Sub1 = models.IntegerField()
     Sub2 = models.IntegerField()   
     Sub3 = models.IntegerField()
     Sub4 = models.IntegerField()
