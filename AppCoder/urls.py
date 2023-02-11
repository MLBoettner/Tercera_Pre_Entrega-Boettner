from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('especialidades/', views.especialidades, name="especialidades"),
    path('pacientes/', views.pacientes, name="pacientes"),
    path('medicos/', views.medicos, name="medicos"),
    path('estudios/', views.estudios, name="estudios"),
]

