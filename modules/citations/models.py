# -*- coding: utf-8 -*-

from django.db import models

from master.models import Master


class Citation(models.Model):
	text = models.TextField(u"Текст цитаты")
	master = models.ForeignKey(Master, verbose_name=u"Автор")

	updated = models.DateTimeField(u"Данные обновлены", auto_now=True,
	                               auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False,
	                               auto_now_add=True)

	@classmethod
	def get_random(cls):
		return cls.objects.values('master__apelido', 'master__name', 'text')\
					.order_by('?').first()

	class Meta:
		verbose_name = u'Цитата'
		verbose_name_plural = u'Цитаты'
