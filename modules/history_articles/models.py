# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q

from search.models import SearchManager


def get_uploaded_file_name(instance, filename):
	return "images/history/%s" % filename


class ArticleManager(SearchManager):
	def get_search_qs(self, q):
		return self.get_queryset().filter(
			Q(title__icontains=q) | Q(detail_text__icontains=q)
		).distinct()


class Article(models.Model):
	title = models.CharField(u"Название", max_length=400)
	photo = models.ImageField(u"Фото", upload_to=get_uploaded_file_name,
	                          blank=True, null=True)
	detail_text = models.TextField(u"Описание", blank=True, null=True)
	preview_text = models.TextField(u"Краткое описание", blank=True, null=True)
	keywords = models.CharField(u"Keywords статьи", max_length=400, blank=True, null=True)
	description = models.CharField(u"Description статьи", max_length=400, blank=True, null=True)
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True,
	                               auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False,
	                               auto_now_add=True)

	objects = ArticleManager()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("article", kwargs={"pk": self.id})

	@property
	def data_for_search(self):
		return {
			'title': self.title,
			'text': self.preview_text or "",
			'href': self.get_absolute_url()
		}

	class Meta:
		verbose_name = u'Статья по капоэйре'
		verbose_name_plural = u'Статьи по капоэйре'
