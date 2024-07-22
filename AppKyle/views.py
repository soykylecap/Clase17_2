from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, "AppKyle/index.html")

def cursos(request):
    return render(request, "AppKyle/cursos.html")

def profesores(request):
    return render(request, "AppKyle/profesores.html")

def estudiantes(request):
    return render(request, "AppKyle/estudiantes.html")

def entregables(request):
    return render(request, "AppKyle/entregables.html")
