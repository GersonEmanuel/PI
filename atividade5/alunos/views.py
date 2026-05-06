from django.shortcuts import render

# Create your views here.

def lista_view(request):
    alunos = [
        {'id': 1, 'nome': 'eu', 'matricula': '2020'},
        {'id': 2, 'nome': 'sou', 'matricula': '2022'}
    ]

    return render(request, "alunos/lista.html")

def novo_view(request):
    return render(request, "alunos/novo.html")

def detalhe_view(request, aluno_id):
    aluno = {'id': aluno_id, 'nome': 'eu', 'matricula': '2020'}

    return render(request, 'alunos/detalhe.html', {'aluno': aluno})


