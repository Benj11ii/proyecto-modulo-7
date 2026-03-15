from django.urls import path
from .views import ListaClientesView,  CrearClienteView, EditarClienteView

urlpatterns = [
    # Definimos la ruta para la lista de clientes
    path('clientes/', ListaClientesView.as_view(), name='lista_clientes'),
    path('clientes/nuevo/', CrearClienteView.as_view(), name='crear_cliente'),
      path('clientes/editar/<int:pk>/', EditarClienteView.as_view(), name='editar_cliente'),
]