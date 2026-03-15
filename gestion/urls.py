from django.urls import path
from .views import ListaClientesView

urlpatterns = [
    # Definimos la ruta para la lista de clientes
    path('clientes/', ListaClientesView.as_view(), name='lista_clientes'),
]