from django.db import models

# Create your models here.

class Viajero(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=8)

class Circuito(models.Model):
    lugar = models.CharField(max_length=30)
    destinos_turisticos = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=900, null=True, blank=True)
    precio = models.IntegerField()
    

    def __str__(self):
        return "Lugar: %s, Destino Turístico: %s, Descripción: %s, Precio: %s" %(self.lugar, self.destinos_turisticos, self.descripcion, self.precio)


class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    concretado = models.BooleanField()