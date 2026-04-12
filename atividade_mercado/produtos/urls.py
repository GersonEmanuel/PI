from django.urls import path
from . import views

app_name = "produtos"

urlpatterns = [
    path("lista/", views.lista_produtos, name="lista_produtos"),
    path("detalhes/<int:produto_uuid>/", views.detalhes_produto, name="detalhes_produto")


]
