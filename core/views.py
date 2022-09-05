from django.shortcuts import render, redirect
from .models import Carros, Detalhacarro, Loja
from .forms import CarrosForm, DetalhacarroForm, LojaForm



def index(request):
    return render (request, 'index.html')

def carros(request):
    return render (request, 'formulario.html')

def loja(request):
    return render (request, 'loja.html')


def detalhar(request):
    return render (request, 'detalhacarro.html')

    
def listar_carros(request):
    carros = Carros.objects.all()
    contexto = {
        'todos_carros': carros
    }
    return render(request, 'index.html', contexto)

def cadastrar_carros(request):
    form = CarrosForm(request.POST or None)

    if form.is_valid():
        form.save()  
        return redirect('listar_carros')
    contexto = {
        'form_carro': form
    }
    return render(request, 'formulario.html', contexto)

def editar_carros(request, id):
    carro = Carros.objects.get(pk=id)

    form = CarrosForm(request.POST or None, instance=carro)
    if form.is_valid():
        form.save()  
        return redirect('listar_carros')
    contexto = {
        'form_carro': form  
    }
    return render(request, 'formulario.html', contexto)

def remover_carros(request, id):
    carro = Carros.objects.get(pk = id) 
    carro.delete()
    return redirect('listar_carros')

def detalhar_carros(request):
    carros =  Carros.objects.all()
    contexto = {
        'detalhar': carros
    }
    return render(request, 'detalhacarro.html', contexto) 

def detalhar_cadastrar(request): 
    form = DetalhacarroForm(request.POST or None) 

    if form.is_valid():
        form.save()
        return redirect('detalhar_carros')

    contexto = {
        'form_carro' : form 
     }

    return render(request, 'detalhar_cadastrar', contexto)

def detalhar_editar(request, id):
    carro = Carros.objects.get(pk=id)

    form = DetalhacarroForm(request.POST or None, instance = carro)

    if form.is_valid():
     form.save()
     return redirect('detalhar_carros')

    contexto = {
        'form_carro' : form 
     }

    return render(request, 'detalhar_cadastrar', contexto)

def detalhar_remover(request, id):
    carro = Carros.objects.get(pk = id)
    carro.delete()
    return redirect('listar_carros')

def listar_loja(request, id):
    loja = Loja.objects.get(pk = id)

    contexto = {
        'loja': loja
    }

    return render(request, 'loja.html', contexto) 

def cadastrar_loja(request):
    form = LojaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_loja')
    contexto = {
    'form_loja': form
  }
    return render(request, 'cadastrar_loja.html', contexto)

def editar_loja(request, id):
    loja = Loja.objects.get(id=id)
    
    form = LojaForm(request.POST or None, instance = loja)

    if form.is_valid():
        form.save()
        return redirect('listar_loja')
    contexto = {
    'form_loja': form
  }
    return render(request, 'cadastrar_loja.html', contexto)


def remover_loja(request, id):
    loja = Loja.objects.get(pk=id) 
    loja.delete()
    return redirect('listar_carros')