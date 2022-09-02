from django.shortcuts import render
from .models import Carros
from .models import Detalhacarro


def index_carros(request):
    objetocarro = Carros.objects.all()
    contexto = {
        'todos_carros': objetocarro
    }
    return render( request, 'index.html', contexto)

def tipos_carros(request):
    variação_carros = Detalhacarro.objects.all()
    contexto = {
        'modelos-carros': variação_carros 
    }
    return render (request, 'formulario.html', contexto)