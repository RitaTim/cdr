from __future__ import unicode_literals
from django.db import models

def get_uploaded_file_name(instance, filename):
	return "images/about/%s" % filename

class About(models.Model):
	title = models.CharField(verbose_name="Заголовок", max_length=100)
	text = models.TextField(verbose_name="Текст", blank=True, null=True)
	img = models.ImageField(upload_to=get_uploaded_file_name, verbose_name="Картинка", blank=True, null=True)

	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)