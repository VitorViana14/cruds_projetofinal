from django.db import models

class Carros(models.Model):
    modelo = models.CharField('Modelo', max_length=130)
    marca = models.CharField('Marca', max_length=100)
    ano = models.IntegerField('Ano') 


class Detalhacarro(models.Model):
    cor = models.CharField('Cor', max_length=130)
    características= models.CharField('Caractrísticas', max_length=100)
    descrição = models.CharField('Descrição', max_length=150) 

class Loja(models.Model):
    cidade = models.CharField('Cidade', max_length=100)
    endereço = models.CharField( 'Endereço', max_length=100)
    unidade = models.ImageField('Unidade')
     
     