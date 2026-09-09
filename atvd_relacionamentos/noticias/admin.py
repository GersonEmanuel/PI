from django.contrib import admin
from .models import Categoria, Noticia, Perfil, Tag

admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Noticia)
admin.site.register(Perfil)
