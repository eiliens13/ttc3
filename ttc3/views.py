from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template 
from django.shortcuts import render


class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def aloha(request): # Primera vista

    p1 = Persona(" Terricola Daily", "Taboada")
    temas_del_curso = ["plantillas", "modelos", "formularios", "vistas", "despliegue"]
    return render(request, "plantilla1.html", {
            "nombre_persona":p1.nombre,
            "apellido_persona":p1.apellido, 
            "tiempo":datetime.datetime.now(),
            "temas":temas_del_curso,
        })

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
    fecha_actual = datetime.datetime.now()
    return render(request, "home.html", {"dame_fecha":fecha_actual})


def layout (request):
    return render(request, "layout.html", {})


def about (request):
    return render(request, "about.html", {})