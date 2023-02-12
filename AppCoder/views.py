from django.shortcuts import render, redirect, HttpResponse
from .models import *
from .forms import *


# Create your views here.
def inicio (request):

    return render(request, "AppCoder/inicio.html")

def especialidades (request):

    if request.method == 'POST':
        mi_formulario=EspecialidadFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            especialidad=Especialidad(nombre=informacion['nombre'], grupoetario=informacion['grupoetario'])
            especialidad.save()
            return redirect('inicio')
    else:
        mi_formulario=EspecialidadFormulario()
        
    return render(request, "AppCoder/especialidades.html", {'especialidades':mi_formulario})

def medicos (request):

    if request.method == 'POST':
        mi_formulario=MedicoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            medicos=Medico(nombre=informacion['nombre'],
                           apellido=informacion['apellido'],
                           email=informacion['email'],
                           profesion=informacion['profesion'],)
            medicos.save()
            return redirect('inicio')
    else:
        mi_formulario=MedicoFormulario()
        
    return render(request, "AppCoder/medicos.html", {'medicos':mi_formulario})

def pacientes (request):
    if request.method == 'POST':
        mi_formulario=PacienteFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            pacientes=Paciente(nombre=informacion['nombre'],
                           apellido=informacion['apellido'],
                           email=informacion['email'])
            pacientes.save()
            return redirect('inicio')
    else:
        mi_formulario=PacienteFormulario()
        
    return render(request, "AppCoder/pacientes.html", {'pacientes':mi_formulario})

def estudios (request):
    if request.method == 'POST':
        mi_formulario=EstudioFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            estudios=Estudio(nombre=informacion['nombre'],
                           fecha=informacion['fecha'],
                           recibido=informacion['recibido'])
            estudios.save() 
            return redirect('inicio')
    else:
        mi_formulario=EstudioFormulario()
        
    return render(request, "AppCoder/estudios.html", {'estudios':mi_formulario})

def buscar (request):

    if request.GET['grupoetario']:
        mi_grupoetario=request.GET['grupoetario']
        resultado=Especialidad.objects.filter(grupoetario__icontains=mi_grupoetario)
        
        return render(request, "AppCoder/inicio.html",{'especialidad':resultado,'grupoetario':mi_grupoetario })
    
    respuesta='No ingresaste datos'

    return HttpResponse(respuesta)   