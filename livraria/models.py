from django.db import models


class Prateleira(models.Model):
    num_prateleira = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=30)
    def __str__(self): return self.categoria


class Vendedor(models.Model):
    registro = models.CharField(max_length=20, primary_key=True)
    nome = models.CharField(max_length=50)
    def __str__(self): return self.nome


class Cliente(models.Model):
    cpf = models.CharField(max_length=20, primary_key=True)
    nome = models.CharField(max_length=80)
    def __str__(self): return self.nome


class Livro(models.Model):
    isbn = models.CharField(max_length=20, primary_key=True)
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    qtd_estoque = models.IntegerField()
    prateleira = models.ForeignKey(Prateleira, on_delete=models.CASCADE)
    def __str__(self): return self.titulo


class Venda(models.Model):
    id_venda = models.AutoField(primary_key=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    livros = models.ManyToManyField(Livro, related_name='vendas')
