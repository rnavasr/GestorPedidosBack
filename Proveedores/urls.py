from django.urls import path
from .views import *

urlpatterns = [
    path('crear_proveedor/', CrearProveedor.as_view(), name='crear_proveedor'),
]
