from __future__ import unicode_literals
from django.db import models
from datetime import datetime

def get_uploaded_file_name(instance, filename):
	return "images/history/%s" % filename

class Article(models.Model):
	title = models.CharField(verbose_name="Название", max_length=400)
	photo = models.ImageField(upload_to=get_uploaded_file_name, verbose_name="Фото", blank=True, null=True)
	description = models.TextField(verbose_name="Описание", blank=True, null=True)
	period = models.CharField(verbose_name="Период", max_length=400, blank=True, null=True)

	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title