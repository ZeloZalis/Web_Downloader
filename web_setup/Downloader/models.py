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

# Para que un registro pueda ser null, se debe agregar dentro del paréntesis
# (blank=True, null=True)
class Data(models.Model):
    website = models.CharField(max_length=10, verbose_name="Website")
    link = models.CharField(max_length=100, verbose_name="Link")
    frmat = models.CharField(max_length=4, verbose_name="Format")

    def __str__(self):
        return f"{self.website} - {self.frmat}"

class User(models.Model):
    user_ip = models.CharField(max_length=20, verbose_name="User IP")
    country = models.CharField(max_length=30, verbose_name="Country")

    def __str__(self):
        return f"{self.country} - {self.user_ip}"

class Download(models.Model):
    date = models.DateField(verbose_name="Date")
    succesful = models.BooleanField()

    def __str__(self):
        return f"{self.date}, succesful: {self.succesful}"