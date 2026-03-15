from django.views.generic import ListView
from .models import Cliente

# Esta vista se encarga de traer todos los clientes de la BD y pasarlos al HTML
class ListaClientesView(ListView):
    model = Cliente
    template_name = 'gestion/lista_clientes.html'
    context_object_name = 'clientes'