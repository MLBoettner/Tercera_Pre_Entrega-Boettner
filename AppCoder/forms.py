from django import forms

class EspecialidadFormulario (forms.Form):

    nombre=forms.CharField()
    grupoetario=forms.IntegerField()

class MedicoFormulario (forms.Form):

    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()
    profesion=forms.CharField()


class PacienteFormulario (forms.Form):

    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()

class EstudioFormulario (forms.Form):

    nombre=forms.CharField()
    fecha=forms.DateField()
    recibido=forms.BooleanField()