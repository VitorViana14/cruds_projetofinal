from django.forms import ModelForm
from core.models import Carros, Detalhacarro, Loja

class CarrosForm(ModelForm):
    class Meta: 
        model = Carros
        fields = ['modelo', 'marca', 'ano']

class Detalhacarro(ModelForm):
    class Meta: 
        model = Detalhacarro 
        fields = ['cor', 'características', 'descrição']
    

class Loja(ModelForm):
    class Meta: 
        model = Loja
        fields = ['cidade', 'enderço', 'unidade']

