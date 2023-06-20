from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=8)

class Circuitos(models.Model):
    nombre = models.CharField(max_length=30)
    destinos_turisticos = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=900, null=True, blank=True)
    precio = models.IntegerField()
    

    def __str__(self):
        return "El nombre es %s, el destino turistico es %s, el precio es %s, la descripcion es %s" %(self.nombre, self.destinos_turisticos, self.descripcion, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    concretado = models.BooleanField()