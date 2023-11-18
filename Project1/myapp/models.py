from django.db import models

# Create your models here.
class Person (models.Model):
    userinputvalue = models.CharField(max_length=30)
    mycalcvalue = models.CharField(max_length=30)
 