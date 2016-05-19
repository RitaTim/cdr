from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from transliterate import translit, detect_language
import time

def get_uploaded_file_name(instance, filename):
	return "gallery/%s" % filename

class Category(models.Model):
	title = models.CharField(verbose_name="Название категории", max_length=400)

	class Meta:
		ordering = ['title',]

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

class Album(models.Model):
	title = models.CharField(verbose_name="Название альбома", max_length=400)
	slug = models.SlugField(unique=True, blank=True, null=True)
	cover = models.ImageField(upload_to=get_uploaded_file_name, verbose_name="Обложка", blank=True, null=True)
	description = models.TextField(verbose_name="Описание альбома", blank=True, null=True)
	category = models.ForeignKey(Category)
	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['updated', 'created']

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('album_detail', None, {'symbol_code': self.slug})

class Photo(models.Model):
	title = models.CharField(verbose_name="Заголовок фото", max_length=400)
	slug = models.SlugField(unique=True, blank=True, null=True)
	comment = models.TextField(verbose_name="Комментарий к фотографии", blank=True, null=True)
	img = models.ImageField(upload_to=get_uploaded_file_name, verbose_name="Картинка")
	album = models.ForeignKey(Album)
	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['updated', 'created']

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('photoy_detail', None, {'symbol_code': self.slug})

def pre_save_post(sender, instance, *args, **kwargs):
	if detect_language(instance.title) == 'ru':
		slug_init = slugify(translit(instance.title, reversed=True))
	else:
		slug_init = slugify(instance.title)
	slug = slug_init
	exists = sender.objects.filter(slug=slug).exists()
	i = 0
	while exists:
		i += 1;
		slug = "%s-%s" % (slug_init, i)
		exists = sender.objects.filter(slug=slug).exists()
	instance.slug = slug

pre_save.connect(pre_save_post, sender=Album)
pre_save.connect(pre_save_post, sender=Photo)


