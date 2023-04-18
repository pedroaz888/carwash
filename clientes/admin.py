

from django.contrib import admin
from .models import Cliente, Carro


class listandoCliente (admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'cpf')
    list_display_links = ('nome',)
   

admin.site.register(Cliente, listandoCliente)


class listandoCarro (admin.ModelAdmin):
    list_display = ('carro', 'placa', 'ano', 'cliente', 'lavagens', 'consertos')
    list_display_links = ('carro',)
   

admin.site.register(Carro, listandoCarro)