from django.urls import path
from . import views

app_name = 'filmes'

urlpatterns = [
    path('', views.filmes_lista_view, name='filme_lista'),
    path('detalhe/', views.filmes_detalhe_view, name='filme_detalhe'),
]
