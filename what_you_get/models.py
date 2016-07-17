# -*- coding: utf-8 -*-

from django.db import models

def get_uploaded_file_name(instance, filename):
	return "icons/%s" % filename

class WhatYouGet(models.Model):
	title = models.CharField(u"Название", max_length=30)
	description = models.TextField(u"Описание", blank=True, null=True)
	icon = models.ImageField(u"Иконка", upload_to=get_uploaded_file_name, blank=True, null=True)
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['updated', 'created']
		verbose_name = u'Что вы получите'
		verbose_name_plural = u'Что вы получите'