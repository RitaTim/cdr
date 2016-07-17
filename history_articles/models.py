# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

def get_uploaded_file_name(instance, filename):
	return "images/history/%s" % filename

class Article(models.Model):
	title = models.CharField(u"Название", max_length=400)
	photo = models.ImageField(u"Фото", upload_to=get_uploaded_file_name, blank=True, null=True)
	description = models.TextField(u"Описание", blank=True, null=True)
	period = models.CharField(u"Период", max_length=400, blank=True, null=True)

	updated = models.DateTimeField(u"Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = u'Историческая статья'
		verbose_name_plural = u'Историческая статьи'