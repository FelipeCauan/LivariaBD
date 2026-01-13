from django.db import models

class Cliente(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

class Atendente(models.Model):
    registro = models.CharField(max_length=50, primary_key=True)
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    cnpj = models.CharField(max_length=18, primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    def __str__(self):
        return self.nome

class Prateleira(models.Model):
    numero = models.IntegerField(primary_key=True)
    genero = models.CharField(max_length=100)
    capacidade = models.IntegerField(default=0) 
    def __str__(self):
        return f"Prateleira {self.numero}"

class Livro(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    titulo = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    genero = models.CharField(max_length=100)
    prateleira = models.ForeignKey(Prateleira, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo