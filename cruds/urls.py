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
from django.conf import settings
from unicodedata import name
from django.conf.urls.static import static
from core import views
from django.urls import path
from core.views import detalhar_carros, listar_carros, cadastrar_carros, editar_carros, detalhar_carros, detalhar_cadastrar, detalhar_editar, listar_loja,  cadastrar_loja, editar_loja




urlpatterns = [
        path('' , views.index),
        path('carros/', listar_carros, name='index_carros'),  
        path('carros_cadastrar/', cadastrar_carros, name='cadastar_carros'),
        path('editar_carros/<int:id>/', editar_carros, name='editar_carros'), 
        path('detalhar_carro/', detalhar_carros, name='detalhar_carro'),
        path('detalhar_cadastar/', detalhar_cadastrar, name='detalhar_cadastrar'), 
        path('detalhar_editar/<int:id>/', detalhar_editar, name='detalhar_editar'),
        path('loja/<int:id>/', listar_loja, name='loja'),
        path('cadastrar_loja/', cadastrar_loja, name='cadastar_loja'), 
        path('editar_loja/<int:id>/', editar_loja, name='editar_loja'),
        path('admin/', admin.site.urls),
        ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
