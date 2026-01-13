from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_livros, name='livros_no_banco'),
]