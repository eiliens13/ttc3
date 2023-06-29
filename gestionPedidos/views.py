from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def busqueda_circuitos(request):
    return render(request, "busqueda_circuitos.html")


def buscar(request):
    if request.GET["cir"]:
        mensaje = "Circuito encontrado: %r" %request.GET["cir"]
    else:
        mensaje = "Debes introducir un destino para mostrarte nuestras ofertas 😉 "
        return HttpResponse(mensaje)