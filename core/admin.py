from django.contrib import admin
from .models import Cliente, Vendedor, Prateleira, Livro, Venda

admin.site.register(Cliente)
admin.site.register(Vendedor)
admin.site.register(Prateleira)
admin.site.register(Livro)
admin.site.register(Venda)