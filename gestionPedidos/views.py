from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from gestionPedidos.models import Circuito

def busqueda_circuitos(request):
    return render(request, "busqueda_circuitos.html")


def buscar(request):
    if "cir" in request.GET:  # Asegúrate de que el parámetro esté en la solicitud
        circuito = request.GET["cir"]
        if len(circuito) > 20:
            mensaje = "Texto de búsqueda demasiado largo"
            return HttpResponse(mensaje)
        else:
            circuitos = Circuito.objects.filter(lugar__icontains=circuito)
            if circuitos.exists():
                return render(request, "resultados_circuitos.html", {"circuitos": circuitos, "query": circuito})
            else:
                mensaje = "No se encontraron circuitos para tu búsqueda."
                return HttpResponse(mensaje)
    else:
        mensaje = "Debes introducir un destino para mostrarte nuestras ofertas 😉"
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
