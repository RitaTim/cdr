# -*- coding: utf-8 -*-

from django.db import models


class Subscriber(models.Model):
	email = models.EmailField (u"E-mail", max_length=400)
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True,
	                               auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False,
	                               auto_now_add=True)

	def __unicode__(self):
		return self.email

	def __str__(self):
		return self.email

	class Meta:
		verbose_name = u'Подписчик'
		verbose_name_plural = u'Подписчики'
