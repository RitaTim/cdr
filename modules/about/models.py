# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.db.models import Q
from search.models import SearchManager


def get_uploaded_file_name(instance, filename):
	return "images/about/%s" % filename


class AboutManager(SearchManager):
	def get_search_qs(self, q):
		return self.get_queryset().filter(
			Q(title__icontains=q) | Q(text__icontains=q)
		).distinct()


class About(models.Model):
	title = models.CharField(u"Заголовок", max_length=100)
	text = models.TextField(u"Текст", blank=True, null=True)
	img = models.ImageField(u"Картинка", upload_to=get_uploaded_file_name,
	                        blank=True, null=True)
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True,
	                               auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False,
	                               auto_now_add=True)

	objects = AboutManager()

	@property
	def data_for_search(self):
		return {
			'title': self.title,
			'url_name': 'about'
		}

	class Meta:
		verbose_name = u'О школе'
		verbose_name_plural = u'О школе'
