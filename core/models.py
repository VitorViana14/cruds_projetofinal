from django.db import models

class Alunos(models.Model):
    nome = models.CharField('nome', max_length=100)
    numero = models.CharField('numero', max_length=11)
    cpf = models.CharField('cpf', max_length=11)

class Funcionarios(models.Model):
    nome = models.CharField('nome', max_length=100)
    numero = models.CharField('numero', max_length=11)
    cref = models.CharField('cref', max_length=6)

class Maquinas(models.Model):
    nome = models.CharField('nome', max_length=100)
    quantidade = models.IntegerField('Vagas') 
    marca = models.CharField('nome', max_length=100)
    equipamento = models.ImageField('equipamento')   
    
