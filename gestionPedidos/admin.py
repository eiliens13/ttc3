from django.contrib import admin
from gestionPedidos.models import Viajero, Circuito, Pedido

# Register your models here.
admin.site.register(Viajero)
admin.site.register(Circuito)
admin.site.register(Pedido)
