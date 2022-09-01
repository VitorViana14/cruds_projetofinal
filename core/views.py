from django.shortcuts import render
from core.forms import Carros


def index(request):
    return render( request, 'index.html')

def form(request):
    data = {}
    data['form'] = Carros()
    return render(request, 'formulario.html', data)