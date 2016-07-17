# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from country.models import Country

def get_uploaded_file_name(instance, filename):
	return "images/masters/%s" % filename

class Master(models.Model):
	name = models.CharField(u"Имя", max_length=400)
	apelido = models.CharField(u"Апелиду", max_length=400, blank=True, null=True)
	country = models.ForeignKey(Country, verbose_name=u"Страна", blank=True, null=True)
	photo = models.ImageField(u"Фото", upload_to=get_uploaded_file_name, blank=True, null=True)
	cordao = models.CharField(u"Шнур", max_length=400, blank=True, null=True)
	biography = models.TextField(u"Биография", blank=True, null=True)
	date_birth = models.DateField(u"Дата рожения", blank=True, null=True)
	date_death = models.DateField(u"Дата смерти", blank=True, null=True)

	updated = models.DateTimeField(u"Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.apelido or self.name

	class Meta:
		verbose_name = u'Мастер'
		verbose_name_plural = u'Мастера'