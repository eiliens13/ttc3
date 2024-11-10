from django.db import models

class Viajero(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="Dirección")
    email = models.EmailField()
    phone = models.CharField(max_length=8)

    def __str__(self):
        return self.nombre


class Circuito(models.Model):
    lugar = models.CharField(max_length=30)
    destinos_turisticos = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=900, null=True, blank=True)
    precio = models.IntegerField()
    imagen_principal = models.URLField(max_length=300, null=True, blank=True)
    destinos_adicionales = models.TextField(null=True, blank=True)
    imagenes_galeria = models.TextField(null=True, blank=True)         

    def __str__(self):
        return "Lugar: %s, Destino Turístico: %s, Descripción: %s, Precio: %s" %(self.lugar, self.destinos_turisticos, self.descripcion, self.precio)


class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    concretado = models.BooleanField()