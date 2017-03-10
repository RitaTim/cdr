# -*- coding: utf-8 -*-

from django.db import models

from filials.models import Filial


class NewStudent(models.Model):
	name = models.CharField(u"ФИО", max_length=400)
	phone = models.CharField(u"Номер телефона", max_length=400)
	filial = models.ForeignKey(Filial, verbose_name=u"Филиал")
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True,
	                               auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False,
	                               auto_now_add=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = u'Запись нового ученика'
		verbose_name_plural = u'Записи новых учеников'
