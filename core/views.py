from django.shortcuts import render

def listar_alunos(request):
    return render(request, 'alunos.html')
