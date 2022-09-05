from django.forms import ModelForm
from .models import Carros, Detalhacarro, Loja

class CarrosForm(ModelForm):
    class Meta: 
        model = Carros
        fields = ['modelo', 'marca', 'ano']

class DetalhacarroForm(ModelForm):
    class Meta: 
        model = Detalhacarro 
        fields = ['cor', 'características', 'descrição']
    

class LojaForm(ModelForm):
    class Meta: 
        model = Loja
        fields = ['cidade', 'endereço', 'unidade']

