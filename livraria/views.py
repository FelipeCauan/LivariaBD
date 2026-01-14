from django.shortcuts import render, redirect
from .models import Livro
from .models import Venda
from django.db.models import Count
from .models import Livro, Venda, Vendedor


def home(request):
    return render(request, 'core/home.html')


def lista_livros(request):
    livros = Livro.objects.select_related('prateleira').all()
    return render(request, 'core/livros.html', {'livros': livros})


def dashboard(request):
    estoque_baixo = Livro.objects.filter(qtd_estoque__lte=5)
    livros_baratos = Livro.objects.filter(preco__lt=50)

    mais_vendidos = Livro.objects.annotate(
        total_vendas=Count('vendas')
    ).order_by('-total_vendas')[:5]

    return render(request, 'core/dashboard.html', {
        'estoque_baixo': estoque_baixo,
        'mais_vendidos': mais_vendidos,
        'livros_baratos': livros_baratos,
    })


def realizar_venda(request):
    if request.method == 'POST':
        # Captura os dados do formulário
        livro_id = request.POST.get('livro')
        vendedor_id = request.POST.get('vendedor')
        valor_venda = request.POST.get('valor')

        # 1. Cria a venda no banco (INSERT)
        livro = Livro.objects.get(isbn=livro_id)
        vendedor = Vendedor.objects.get(registro=vendedor_id)

        nova_venda = Venda.objects.create(
            vendedor=vendedor,
            Valor=valor_venda
        )
        nova_venda.livros.add(livro)  # Relacionamento ManyToMany

        # 2. Atualiza o estoque (UPDATE)
        if livro.qtdEstoque > 0:
            livro.qtdEstoque -= 1
            livro.save()

        return redirect('dashboard')

    # Busca dados para os selects do formulário
    context = {
        # Apenas livros com estoque
        'livros': Livro.objects.filter(qtdEstoque__gt=0),
        'vendedores': Vendedor.objects.all(),
    }
    return render(request, 'core/venda.html', context)
