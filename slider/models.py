# -*- coding: utf-8 -*-

from django.db import models

def get_uploaded_file_name(instance, filename):
	return "images/slider/%s" % filename

class Slider(models.Model):
	name = models.CharField(u"Название", max_length=30, blank=True, null=True)
	is_main = models.BooleanField(u"Главный слайд", default=False)
	img = models.ImageField(u"Картинка", upload_to=get_uploaded_file_name)
	title_h1 = models.CharField(u"Главный заголовок", max_length=30, blank=True, null=True)
	title_h2 = models.CharField(u"Заголовок второго уровня", max_length=50, blank=True, null=True)
	title_btn = models.CharField(u"Название кнопки", max_length=10, blank=True, null=True)
	href_btn = models.CharField(u"Ссылка кнопки", max_length=40, blank=True, null=True)
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-updated', '-created']
		verbose_name = u'Слайдер'
		verbose_name_plural = u'Слайдеры'