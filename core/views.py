from django.shortcuts import render
from core.forms import CarrosForm


def index(request):
    return render( request, 'index.html')

def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request, 'formulario.html', data)