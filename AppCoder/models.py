from django.db import models

# Create your models here.
class Especialidad (models.Model):
    
    nombre=models.CharField(max_length=40)
    # Grupo etario  1 (ninos) 2 (adolecentes) 3 (adultos) 4 (adultos mayores)
    grupoetario=models.IntegerField()

    def __str__(self):
        return self.nombre

class Paciente (models.Model):

    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()

class Medico (models.Model):

    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)

class Estudio (models.Model):

    nombre=models.CharField(max_length=30)
    fecha=models.DateField()
    recibido=models.BooleanField()

