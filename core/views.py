from django.shortcuts import render
from .models import Carros
from .models import Detalhacarro
from core.models import Carros



def index_carros(request):
    objetocarro = Carros.objects.all()
    contexto = {
        'todos_carros': objetocarro
    }
    return render( request, 'index.html', contexto)

def tipos_carros(request):
    variação_carros = Detalhacarro.objects.all()
    contexto = {
        'modelos_carros': variação_carros 
    }
    return render (request, 'formulario.html', contexto)

def create(request):
    form = tipos_carros(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_carros')
    
def view(request, pk):
    data = {}
    data[''] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data[''] = Carros.objects.get(pk=pk)
    data['form'] = tipos_carros(instance=data[''])
    return render(request, 'formulario.html', data)
