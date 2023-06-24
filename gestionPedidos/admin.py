from django.contrib import admin
from gestionPedidos.models import Viajero, Circuito, Pedido

# Register your models here.

class ViajeroAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion", "email", "phone")
    search_fields = ("nombre", "phone")


class CircuitosAdmin(admin.ModelAdmin):
    list_filter = ("lugar", )


class PedidosAdmin(admin.ModelAdmin):
    list_display = ("numero", "fecha")
    list_filter = ("fecha",)
    date_hierarchy = "fecha"

admin.site.register(Viajero, ViajeroAdmin)
admin.site.register(Circuito, CircuitosAdmin)
admin.site.register(Pedido, PedidosAdmin)
