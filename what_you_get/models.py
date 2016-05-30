from __future__ import unicode_literals
from django.db import models

def get_uploaded_file_name(instance, filename):
	return "icons/%s" % filename

class WhatYouGet(models.Model):
	title = models.CharField(verbose_name="Название", max_length=30)
	description = models.TextField(verbose_name="Описание", blank=True, null=True)
	icon = models.ImageField(upload_to=get_uploaded_file_name, verbose_name="Иконка", blank=True, null=True)
	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['updated', 'created']
