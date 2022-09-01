from django.shortcuts import render

def inicio(request):
    return render(request, 'inicial.html')

def aluno(request):
    return render(request, 'aluno.html')
