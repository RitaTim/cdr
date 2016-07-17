# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

def get_uploaded_file_name(instance, filename):
	return "images/about/%s" % filename

class About(models.Model):
	title = models.CharField(u"Заголовок", max_length=100)
	text = models.TextField(u"Текст", blank=True, null=True)
	img = models.ImageField(u"Картинка", upload_to=get_uploaded_file_name, blank=True, null=True)

	updated = models.DateTimeField(u"Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False, auto_now_add=True)

	class Meta:
		verbose_name = u'О школе'
		verbose_name_plural = u'О школе'