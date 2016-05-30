from __future__ import unicode_literals
from django.db import models

def get_uploaded_file_name(instance, filename):
	return "images/slider/%s" % filename

class Slider(models.Model):
	name = models.CharField(verbose_name="Название", max_length=30, blank=True, null=True)
	is_main = models.BooleanField(verbose_name="Главный слайд", default=False)
	img = models.ImageField(upload_to=get_uploaded_file_name, verbose_name="Картинка")
	title_h1 = models.CharField(verbose_name="Главный заголовок", max_length=30, blank=True, null=True)
	title_h2 = models.CharField(verbose_name="Заголовок второго уровня", max_length=50, blank=True, null=True)
	title_btn = models.CharField(verbose_name="Название кнопки", max_length=10, blank=True, null=True)
	href_btn = models.CharField(verbose_name="Ссылка кнопки", max_length=40, blank=True, null=True)
	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-updated', '-created']