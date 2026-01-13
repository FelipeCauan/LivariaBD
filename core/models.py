from django.db import models

class Cliente(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    registro = models.CharField(max_length=50, primary_key=True)
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

class Prateleira(models.Model):
    numPrateleira = models.IntegerField(primary_key=True)
    categoria = models.CharField(max_length=100)
    def __str__(self):
        return f"Prateleira {self.numPrateleira}"
    
class Livro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    qtdEstoque = models.IntegerField(default=0)
    prateleira = models.ForeignKey(Prateleira, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.titulo
    
class Venda(models.Model):
    idVenda = models.AutoField(primary_key=True)
    Valor = models.DecimalField(max_digits=10, decimal_places=2)
    livros = models.ManyToManyField(Livro, related_name='vendas')