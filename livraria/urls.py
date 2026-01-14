from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.lista_livros, name='lista_livros'),
    path('', views.home, name='home'),
    path('livros/', views.lista_livros, name='lista_livros'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('venda/nova/', views.realizar_venda, name='realizar_venda'),
]
