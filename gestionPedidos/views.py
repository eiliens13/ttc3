from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Circuito


# Create your views here.
def busqueda_circuitos(request):
    return render(request, "busqueda_circuitos.html")


def buscar(request):
    if request.GET["cir"]:
        # mensaje = "Circuito encontrado: %r" %request.GET["cir"]
        circuito = request.GET["cir"]
        if len(circuito)>20:
            mensaje = "Texto de busqueda demasaido largo"
        else:
            circuitos = Circuito.objects.filter(lugar__icontains=circuito)
            return render(request, "resultados_circuitos.html", {"circuitos":circuitos, "query":circuito})
    else:
        mensaje = "Debes introducir un destino para mostrarte nuestras ofertas 😉 "
    return HttpResponse(mensaje)