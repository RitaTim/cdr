from __future__ import unicode_literals
from django.db import models

from trainers.models import Trainer

class Filial(models.Model):
	CITIES = (
		('Rostov', 'Ростов-на-Дону'),
		('Cimlyansk', 'Цимлянск'),
		('Shahty', 'Шахты'),
	)
	city = models.CharField(verbose_name="Город", max_length=300, choices=CITIES, default='Rostov')
	address = models.CharField(verbose_name="Адрес", max_length=300, blank=True, null=True)
	map_coord_x = models.FloatField(verbose_name="Координата х на карте", blank=True, null=True)
	map_coord_y = models.FloatField(verbose_name="Координата у на карте", blank=True, null=True)
	email = models.CharField(verbose_name="E-mail", max_length=300, blank=True, null=True)
	phone = models.CharField(verbose_name="Телефон", max_length=300)
	timetable_adults = models.TextField(verbose_name="Расписание (взрослые)", blank=True, null=True)
	timetable_children = models.TextField(verbose_name="Расписание (дети)", blank=True, null=True)
	trainer = models.ManyToManyField(Trainer, verbose_name="Тренер", related_name="filial", related_query_name="filial", blank=True)
	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['id',]