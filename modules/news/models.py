# -*- coding: utf-8 -*-

from transliterate import translit, detect_language

from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from search.models import SearchManager

def get_uploaded_file_name(instance, filename):
	return "news/%s" % filename


class NewManager(SearchManager):
	def get_search_qs(self, q):
		return self.get_queryset().filter(
			Q(title__icontains=q) |
			Q(preview_text__icontains=q) |
			Q(detail_text__icontains=q)
		).distinct()


class New(models.Model):
	title = models.CharField(u"Название", max_length=100)
	slug = models.SlugField(unique=True, blank=True, null=True)
	preview_text = models.TextField(u"Описание анонса")
	detail_text = models.TextField(u"Детальное описание")
	image = models.ImageField(u"Картинка", upload_to=get_uploaded_file_name, blank=True, null=True)
	keywords = models.CharField(u"Keywords статьи", max_length=400, blank=True, null=True)
	description = models.CharField(u"Description статьи", max_length=400, blank=True, null=True)
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False,
	                               auto_now_add=True)

	objects = NewManager()

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("new_detail", kwargs={"slug": self.slug})

	@property
	def data_for_search(self):
		return {
			'title': self.title,
			'text': self.preview_text,
			'href': self.get_absolute_url()
		}


	class Meta:
		ordering = ['-updated', '-created']
		verbose_name = u'Новость'
		verbose_name_plural = u'Новости'


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
		i += 1
		slug = "%s-%s" % (slug_init, i)
		exists = sender.objects.filter(slug=slug).exists()
	instance.slug = slug

pre_save.connect(pre_save_post, sender=New)
