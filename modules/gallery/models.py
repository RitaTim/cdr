# -*- coding: utf-8 -*-

from transliterate import translit, detect_language

from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.utils.text import slugify

from search.models import SearchManager


def get_uploaded_file_name(instance, filename):
	return "gallery/%s" % filename

class Category(models.Model):
	title = models.CharField(u"Название категории", max_length=400)

	class Meta:
		ordering = ['title',]

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = u'Тип альбомов'
		verbose_name_plural = u'Тип альбомов'


class AlbumManager(SearchManager):
	def get_search_qs(self, q):
		return self.get_queryset().filter(
			Q(title__icontains=q) |
			Q(description__icontains=q)
		).distinct()


class Album(models.Model):
	title = models.CharField(u"Название альбома", max_length=400)
	slug = models.SlugField(unique=True, blank=True, null=True)
	cover = models.ImageField(u"Обложка", upload_to=get_uploaded_file_name,
	                          blank=True, null=True)
	description = models.TextField(u"Описание альбома", blank=True, null=True)
	category = models.ForeignKey(Category)
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True,
	                               auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False,
	                               auto_now_add=True)

	objects = AlbumManager()

	class Meta:
		ordering = ['updated', 'created']

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('album_detail', None, {'symbol_code': self.slug})

	@property
	def data_for_search(self):
		return {
			'title': self.title,
			'text': self.description,
			'href': self.get_absolute_url()
		}

	class Meta:
		verbose_name = u'Альбом'
		verbose_name_plural = u'Альбомы'

class Photo(models.Model):
	title = models.CharField(u"Заголовок фото", max_length=400, blank=True,
	                         null=True)
	comment = models.TextField(u"Комментарий к фотографии", blank=True,
	                           null=True)
	img = models.ImageField(u"Картинка", upload_to=get_uploaded_file_name)
	album = models.ForeignKey(Album)
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True,
	                               auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False,
	                               auto_now_add=True)

	class Meta:
		ordering = ['updated', 'created']

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('photoy_detail', None, {'symbol_code': self.slug})

	class Meta:
		verbose_name = u'Фото'
		verbose_name_plural = u'Фото'

def pre_save_post(sender, instance, *args, **kwargs):
	if instance.slug:
		slug_init = instance.slug
	else:
		if detect_language(instance.title) == 'ru':
			slug_init = slugify(translit(instance.title, reversed=True))
		else:
			slug_init = slugify(instance.title)

	slug = slug_init
	exists = sender.objects.filter(slug=slug).exclude(id=instance.id).exists()
	i = 0
	while exists:
		i += 1;
		slug = "%s-%s" % (slug_init, i)
		exists = sender.objects.filter(slug=slug).exists()
	instance.slug = slug

pre_save.connect(pre_save_post, sender=Album)
