from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from master.models import Master

class Citation(models.Model):
	text = models.TextField(verbose_name="Текст цитаты")
	master = models.ForeignKey(Master, verbose_name="Автор")

	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.name