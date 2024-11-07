from django.shortcuts import render, get_object_or_404
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


def contacto(request):
    if request.method=="POST":
        return render(request, "gracias.html") 
    return render(request, "contacto.html")  

def detalles_circuito(request, id):
    # Obtener el circuito por ID o devolver un 404 si no existe
    circuito = get_object_or_404(Circuito, id=id)
    # Pasar el objeto 'circuito' a la plantilla
    return render(request, 'circuitos/detalles_circuito.html', {'circuito': circuito})
