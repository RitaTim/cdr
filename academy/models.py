from __future__ import unicode_literals
from django.db import models

class Academy(models.Model):
	title = models.CharField(verbose_name="Заголовок", max_length=400)
	description = models.TextField(verbose_name="Описание", blank=True, null=True)
	ref_video = models.CharField(verbose_name="Видео", max_length=400, blank=True, null=True)
	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

class Section(models.Model):
	title = models.CharField(verbose_name="Название раздела", max_length=400)
	description = models.TextField(verbose_name="Описание", blank=True, null=True)
	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['created']

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

class Subsection(models.Model):
	title = models.CharField(verbose_name="Название подраздела", max_length=400)
	section = models.ForeignKey(Section, verbose_name="Раздел")
	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['created']

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

class Video(models.Model):
	title = models.CharField(verbose_name="Название видео", max_length=400)
	ref_video = models.CharField(verbose_name="Ссылка на видео", max_length=400)
	subsection = models.ForeignKey(Subsection, verbose_name="Подраздел")
	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['created']

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title