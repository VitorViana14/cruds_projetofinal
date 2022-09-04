"""cruds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import listar_carros, cadastrar_carros, editar_carros, remover_carros, detalhar_carro, detalhar_cadastar, detalhar_editar, detalhar_remover, listar_loja,  cadastrar_loja, editar_loja, remover_loja  




urlpatterns = [
        path('carros/', listar_carros, name='index_carros'),  
        path('carros_cadastrar/', cadastrar_carros, name='cadastar_carros'),
        path('editar_carros/<int:id>/', editar_carros, name='editar_carros'), 
        path('remover_carros/<int:id>/', remover_carros, name='remover_carros'), 
        path('detalhar_carro/', detalhar_carro, name='detalhar_carro'),
        path('detalhar_cadastar/', detalhar_cadastar, name='detalhar_cadastrar'), 
        path('detalhar_editar/<int:id>/', detalhar_editar, name='detalhar_editar'),
        path('detalhar_remover/<int:id>/', detalhar_remover, name='detalhar_remover'),
        path('loja/</', listar_loja, name='loja'),
        path('cadastrar_loja/', cadastrar_loja, name='cadastar_loja'), 
        path('editar_loja/<int:id>/', editar_loja, name='editar_loja'),
        path('remover_loja/<int:id>/', remover_loja, name='remover_loja'),
        path('admin/', admin.site.urls),
]
