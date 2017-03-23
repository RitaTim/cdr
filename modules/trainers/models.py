# -*- coding: utf-8 -*-

from django.db import models


def get_uploaded_file_name(instance, filename):
	return "trainers/%s" % filename

class Trainer(models.Model):
	name = models.CharField(u"Имя", max_length=200)
	apelido = models.CharField(u"Апелиду", max_length=200, blank=True,
	                           null=True)
	status = models.CharField(u"Статус", max_length=500, blank=True, null=True)
	photo = models.ImageField(u"Фото", upload_to=get_uploaded_file_name,
	                          blank=True, null=True)
	biography = models.TextField(u"Биография", blank=True, null=True)
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True,
	                               auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False,
	                               auto_now_add=True)

	def __str__(self):
		return self.apelido or self.name

	class Meta:
		verbose_name = u'Инструктора'
		verbose_name_plural = u'Инструктор'
