from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Cliente

# Esta vista se encarga de traer todos los clientes de la BD y pasarlos al HTML
class ListaClientesView(ListView):
    model = Cliente
    template_name = 'gestion/lista_clientes.html'
    context_object_name = 'clientes'

class CrearClienteView(CreateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('lista_clientes')

class EditarClienteView(UpdateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    template_name = 'gestion/cliente_form.html'
    success_url = reverse_lazy('lista_clientes')