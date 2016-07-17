# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

def get_uploaded_file_name(instance, filename):
	return "images/country_flag/%s" % filename

class Country(models.Model):
	name = models.CharField(u"Название", max_length=400)
	logo = models.ImageField(upload_to=get_uploaded_file_name, verbose_name=u"Флаг", blank=True, null=True)

	updated = models.DateTimeField(u"Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = u'Страна'
		verbose_name_plural = u'Страны'