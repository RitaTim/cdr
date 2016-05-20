from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from country.models import Country

def get_uploaded_file_name(instance, filename):
	return "images/masters/%s" % filename

class Master(models.Model):
	name = models.CharField(verbose_name="Имя", max_length=400)
	apelido = models.CharField(verbose_name="Апелиду", max_length=400, blank=True, null=True)
	country = models.ForeignKey(Country, verbose_name="Страна", blank=True, null=True)
	photo = models.ImageField(upload_to=get_uploaded_file_name, verbose_name="Фото", blank=True, null=True)
	cordao = models.CharField(verbose_name="Шнур", max_length=400, blank=True, null=True)
	biography = models.TextField(verbose_name="Биография", blank=True, null=True)
	date_birth = models.DateTimeField(verbose_name="Дата рожения", blank=True, null=True)
	date_death = models.DateTimeField(verbose_name="Дата смерти", blank=True, null=True)

	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.apelido or self.name