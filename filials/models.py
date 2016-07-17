# -*- coding: utf-8 -*-

from django.db import models

from trainers.models import Trainer

class Filial(models.Model):
	CITIES = (
		('Rostov', u'Ростов-на-Дону'),
		('Cimlyansk', u'Цимлянск'),
		('Shahty', u'Шахты'),
	)
	city = models.CharField(u"Город", max_length=300, choices=CITIES, default='Rostov')
	address = models.CharField(u"Адрес", max_length=300, blank=True, null=True)
	map_coord_x = models.FloatField(u"Координата х на карте", blank=True, null=True)
	map_coord_y = models.FloatField(u"Координата у на карте", blank=True, null=True)
	email = models.CharField(u"E-mail", max_length=300, blank=True, null=True)
	phone = models.CharField(u"Телефон", max_length=300)
	timetable_adults = models.TextField(u"Расписание (взрослые)", blank=True, null=True)
	timetable_children = models.TextField(u"Расписание (дети)", blank=True, null=True)
	trainer = models.ManyToManyField(Trainer, verbose_name=u"Тренер", related_name="filial", related_query_name="filial", blank=True)
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['id',]

	def __unicode__(self):
		return self.city

	def __str__(self):
		return self.city

	class Meta:
		verbose_name = u'Филиал'
		verbose_name_plural = u'Филиалы'