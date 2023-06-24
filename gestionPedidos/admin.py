from django.contrib import admin
from gestionPedidos.models import Viajeros, Circuitos, Pedidos

# Register your models here.
admin.site.register(Viajeros)
admin.site.register(Circuitos)
admin.site.register(Pedidos)
