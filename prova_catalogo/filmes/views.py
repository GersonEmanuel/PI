from django.shortcuts import render

def filmes_lista_view(request):
    return render(request, 'filmes/filme_lista.html')

def filmes_detalhe_view(request):
    return render(request, 'filmes/filme_detalhe.html')