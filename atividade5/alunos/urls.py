
from django.urls import path
from . import views

app_name="alunos"

urlpatterns = [
    path("", views.lista_view, name="lista_alunos"),
    path("novo/", views.novo_view, name="novo_aluno"),
    path("<int:id_aluno>/", views.detalhe_view, name="detalhe_aluno")

]
