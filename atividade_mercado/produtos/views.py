from django.shortcuts import get_object_or_404, render

from .models import Produto

# Create your views here.

def lista_produtos(request):
    produtos = Produto.objects.all().order_by("UUID")
    return render(request, "produtos/lista_produtos.html", {"produtos": produtos})


def detalhes_produto(request, produto_uuid: int):
    produto = get_object_or_404(Produto, pk=produto_uuid)
    return render(request, "produtos/detalhes_produto.html", {"produto": produto})

