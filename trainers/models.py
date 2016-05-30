from __future__ import unicode_literals
from django.db import models

def get_uploaded_file_name(instance, filename):
	return "trainers/%s" % filename

class Trainer(models.Model):
	name = models.CharField(verbose_name="Имя", max_length=200)
	apelido = models.CharField(verbose_name="Апелиду", max_length=200, blank=True, null=True)
	status = models.CharField(verbose_name="Статус", max_length=500, blank=True, null=True)
	photo = models.ImageField(verbose_name="Фото", upload_to=get_uploaded_file_name, blank=True, null=True)
	biography = models.TextField(verbose_name="Биография", blank=True, null=True)
	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.apelido or self.name