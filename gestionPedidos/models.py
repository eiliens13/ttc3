from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=8)

class Circuitos(models.Model):
    nombre = models.CharField(max_length=30)
    destinos_turisticos = models.CharField(max_length=20)
    precio = models.IntegerField()

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    concretado = models.BooleanField()