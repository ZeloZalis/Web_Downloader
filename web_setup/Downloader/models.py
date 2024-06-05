from django.db import models

# Create your models here.
# Cada tabla de la base de datos es creada a través de una clase, por ende, la clase es la tabla

# Para hacer inserts en la tabla, se tiene que ir a la carpeta e importar la tabla en la que se hará
# Ejemplo: https://paste.ofcode.org/wfjVE5tqiACUdeRSTXrHjH

# También se puede actualizar la información de un registro de la siguiente forma:
# https://paste.ofcode.org/BaLsz8iLZ2rNmRJCFWMyx6

# Para borrar un registro, primero se le hace un get para meterlo a una variable y luego poder borrarlo
# https://paste.ofcode.org/FapvxZWPerRztPfCwfw5tm
# De igual manera es preferible tener un programa externo para visualizar las tablas com DBeaver

# De la siguiente forma se puede hacer un SELECT * desde la misma consola:
# https://paste.ofcode.org/TNwQpj86iB7UQ46vcgzzgr

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