from django.db import models

# Create your models here.

class Familia(models.Model):

    nombre=models.CharField(max_length=50)
    fNacimiento=models.CharField(max_length=7)
    edad=models.IntegerField()
    
