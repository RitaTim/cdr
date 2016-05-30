from __future__ import unicode_literals
from django.db import models

from filials.models import Filial

class NewStudent(models.Model):
	name = models.CharField(verbose_name="ФИО", max_length=400)
	phone = models.CharField(verbose_name="Номер телефона", max_length=400)
	filial = models.ForeignKey(Filial, verbose_name="Филиал")
	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name