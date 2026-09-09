from django.views.generic import DetailView, ListView

from .models import Categoria, Noticia, Tag


class CategoriaListView(ListView):
	model = Categoria
	template_name = 'noticias/lista.html'
	context_object_name = 'objetos'
	extra_context = {'titulo': 'Categorias'}


class TagListView(ListView):
	model = Tag
	template_name = 'noticias/lista.html'
	context_object_name = 'objetos'
	extra_context = {'titulo': 'Tags'}


class NoticiaListView(ListView):
	model = Noticia
	template_name = 'noticias/lista.html'
	context_object_name = 'objetos'
	extra_context = {'titulo': 'Notícias'}

	def get_queryset(self):
		return Noticia.objects.select_related('categoria').prefetch_related('tags')


class CategoriaDetailView(DetailView):
	model = Categoria
	template_name = 'noticias/detalhe.html'
	context_object_name = 'objeto'


class TagDetailView(DetailView):
	model = Tag
	template_name = 'noticias/detalhe.html'
	context_object_name = 'objeto'


class NoticiaDetailView(DetailView):
	model = Noticia
	template_name = 'noticias/detalhe.html'
	context_object_name = 'objeto'
