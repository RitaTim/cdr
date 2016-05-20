from __future__ import unicode_literals
from django.db import models
from datetime import datetime

def get_uploaded_file_name(instance, filename):
	return "images/country_flag/%s" % filename

class Country(models.Model):
	name = models.CharField(verbose_name="Название", max_length=400)
	logo = models.ImageField(upload_to=get_uploaded_file_name, verbose_name="Флаг", blank=True, null=True)

	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name