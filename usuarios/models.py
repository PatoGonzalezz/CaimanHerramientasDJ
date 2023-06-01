from django.db import models

# Create your models here.

class herramientaEl(models.Model):
    id_herraEl = models.CharField(primary_key = True   , max_length= 10)
    nombre_herraEl  = models.CharField(max_length=20)
    precio_herraEl  = models.CharField(max_length=10000000)

    def __str__(self):
        return str(self.id_herraEl ) + " " +str(self.nombre_herraEl)

class herramientaIn(models.Model):
    id_herraIn = models.CharField(primary_key = True   , max_length= 10)
    nombre_herraIn  = models.CharField(max_length=20)
    precio_herraIn  = models.CharField(max_length=10000000)

    def __str__(self):
        return str(self.id_herraIn ) + " " +str(self.nombre_herraIn)

class accesorio(models.Model):
    id_accesorio = models.CharField(primary_key = True   , max_length= 10)
    nombre_accesorio  = models.CharField(max_length=20)
    precio_accesorio  = models.CharField(max_length=10000000)

    def __str__(self):
        return str(self.id_accesorio ) + " " +str(self.nombre_accesorio)
