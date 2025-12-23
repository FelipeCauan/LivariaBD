from django.contrib import admin
from .models import Cliente, Atendente, Fornecedor, Prateleira, Livro

admin.site.register(Cliente)
admin.site.register(Atendente)
admin.site.register(Fornecedor)
admin.site.register(Prateleira)
admin.site.register(Livro)