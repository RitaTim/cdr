from __future__ import unicode_literals
from django.db import models

class Subscriber(models.Model):
	email = models.EmailField (verbose_name="E-mail", max_length=400)
	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.email

	def __str__(self):
		return self.email