from django.forms import ModelForm
from core.models import Carros, Detalhacarro, Loja

class CarrosForm(ModelForm):
    class Meta: 
        model = Carros
        fields = ['Modelo', 'Marca', 'Ano']

class DetalhacarroForm(ModelForm):
    class Meta: 
        model = Detalhacarro 
        fields = ['Cor', 'Características', 'Descrição']
    

class LojaForm(ModelForm):
    class Meta: 
        model = Loja
        fields = ['Cidade', 'Endereço', 'Unidade']

