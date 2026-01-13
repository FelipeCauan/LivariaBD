from django.shortcuts import render
from .models import Livro  

def lista_livros(request):
    todos_os_livros = Livro.objects.all() 
    
    return render(request, 'core/livros.html', {'livros': todos_os_livros})