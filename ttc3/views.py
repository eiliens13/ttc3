from django.http import HttpResponse
import datetime
from django.template import Template, Context


def aloha(request): # Primera vista

    doc_externo = open("C:/Users/Putizima Ama/Desktop/TawaTaxiV1.3/ttc3/ttc3/templates/plantilla1.html")
    nombre = "Daily"
    apellido = "Taboada"
    tiempo = datetime.datetime.now()
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context(
        {
            "nombre_persona":nombre,
            "apellido_persona":apellido,
            "fecha_actual":tiempo,
        }
        )
    documento = plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego bees")


def dame_fecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" %fecha_actual

    return HttpResponse(documento)

def calcula_edad(request, edad, agno):

    #edadActual = 18
    periodo = agno-2019
    edadFutura = edad + periodo
    documento = "<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)

    return HttpResponse(documento)

#=======================================================
# Plantillas de la version 1.2 de Tawa Taxi ;)
def home (request):
    doc_externo = open("C:/Users/Putizima Ama/Desktop/TawaTaxiV1.3/ttc3/ttc3/templates/home.html")
    
    plt = Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def layout (request):
    doc_externo = open("C:/Users/Putizima Ama/Desktop/TawaTaxiV1.3/ttc3/ttc3/templates/layout.html")
    
    plt = Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)

def about (request):
    doc_externo = open("C:/Users/Putizima Ama/Desktop/TawaTaxiV1.3/ttc3/ttc3/templates/about.html")
    
    plt = Template(doc_externo.read())
    
    doc_externo.close()
    
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)