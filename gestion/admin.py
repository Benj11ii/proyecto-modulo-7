from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion

# Configuración personalizada para Cliente
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email')

# Registrar los modelos
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Cuenta)
admin.site.register(Transaccion)