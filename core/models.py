from django.db import models

class Alunos(models.Model):
    nome = models.CharField('Título', max_length=100)
    numero = models.CharField('Título', max_length=11)
    cpf = models.CharField('Título', max_length=11)

class Funcionarios(models.Model):
    nome = models.CharField('Título', max_length=100)
    numero = models.CharField('Título', max_length=11)
    cref = models.CharField('Título', max_length=6)

class Maquinas(models.Model):
    nome = models.CharField('Título', max_length=100)
    numero = models.CharField('Título', max_length=11)    
    
