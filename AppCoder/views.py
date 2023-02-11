from django.shortcuts import render

# Create your views here.
def inicio (request):
    return render(request, "AppCoder/inicio.html")

def especialidades (request):
    return render(request, "AppCoder/especialidades.html")

def medicos (request):
    return render(request, "AppCoder/medicos.html")

def pacientes (request):
    return render(request, "AppCoder/pacientes.html")

def estudios (request):
    return render(request, "AppCoder/estudios.html")