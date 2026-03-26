from django.shortcuts import render


def home_view(request):
    return render(request, "index.html")

def sobre_view(request):
    return render(request, "sobre.html")