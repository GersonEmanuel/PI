from django.urls import path

from .views import (
    CategoriaDetailView,
    CategoriaListView,
    NoticiaDetailView,
    NoticiaListView,
    TagDetailView,
    TagListView,
)

urlpatterns = [
    path('', NoticiaListView.as_view(), name='inicio'),
    path('categorias/', CategoriaListView.as_view(), name='categoria-lista'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detalhe'),
    path('tags/', TagListView.as_view(), name='tag-lista'),
    path('tags/<int:pk>/', TagDetailView.as_view(), name='tag-detalhe'),
    path('noticias/', NoticiaListView.as_view(), name='noticia-lista'),
    path('noticias/<int:pk>/', NoticiaDetailView.as_view(), name='noticia-detalhe'),
]