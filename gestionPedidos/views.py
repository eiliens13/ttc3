from django.shortcuts import render

# Create your views here.
def busqueda_circuitos(request):
    return render(request, "busqueda_circuitos.html")