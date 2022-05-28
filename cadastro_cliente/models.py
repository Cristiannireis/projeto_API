from django.db import models

# Create your models here.



class cadastro_cliente(models.Model):
    nome = models.CharField(max_length=30)
    Rg = models.CharField(max_length=10)
    Inicio_tratamento = models.TextField(max_length=100)
    Numero_sessao = models.CharField(max_length=50)

