from django.forms import ModelForm
from core.models import Carros, Detalhacarro, Loja

class Carros(ModelForm):
    class Meta: 
        model = Carros
        fields = ['Modelo', 'Marca', 'Ano']

class Detalhacarro(ModelForm):
    class Meta: 
        model = Detalhacarro 
        fields = ['Cor', 'Características', 'Descrição']
    

class Loja(ModelForm):
    class Meta: 
        model = Loja
        fields = ['Cidade', 'Endereço', 'Unidade']

