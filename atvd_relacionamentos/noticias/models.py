from django.db import models


class Categoria(models.Model):
	nome = models.CharField(max_length=100)

	class Meta:
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'

	def __str__(self):
		return self.nome

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('categoria-detalhe', args=[self.pk])


class Tag(models.Model):
	titulo = models.CharField(max_length=100)

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('tag-detalhe', args=[self.pk])


class Noticia(models.Model):
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='noticias')
	tags = models.ManyToManyField(Tag, blank=True, related_name='noticias')

	class Meta:
		verbose_name = 'Notícia'
		verbose_name_plural = 'Notícias'

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('noticia-detalhe', args=[self.pk])


class Perfil(models.Model):
	usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='perfil')
	bio = models.TextField()

	def __str__(self):
		return f'Perfil de {self.usuario.username}'
