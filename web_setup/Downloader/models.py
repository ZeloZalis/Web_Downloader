from django.db import models

# Create your models here.
# Cada tabla de la base de datos es creada a través de una clase, por ende, la clase es la tabla
class Data(models.Model):
    website = models.CharField(max_length=10)
    link = models.CharField(max_length=100)
    frmat = models.CharField(max_length=4)

class User(models.Model):
    user_ip = models.CharField(max_length=20)
    country = models.CharField(max_length=30)

class Download(models.Model):
    date = models.DateField()
    succesful = models.BooleanField()