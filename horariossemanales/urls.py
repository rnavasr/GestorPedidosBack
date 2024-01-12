from django.urls import path
from .views import *
DetallesHorarioView
urlpatterns = [
    path('CrearHorarioSucursal/', CrearHorarioSucursal.as_view(), name='CrearHorarioSucursal'),
    path('get/<int:id_horario>', DetallesHorarioView.as_view(), name='DetallesHorarioView'),
]