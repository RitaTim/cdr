# -*- coding: utf-8 -*-

from django.db import models

def get_uploaded_file_name(instance, filename):
	return "images/academy/%s" % filename

class Academy(models.Model):
	title = models.CharField(u"Заголовок", max_length=400)
	description = models.TextField(u"Описание", blank=True, null=True)
	ref_video = models.CharField(u"Видео", max_length=400, blank=True, null=True)
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = u'Академия'
		verbose_name_plural = u'Академия'

class Section(models.Model):
	title = models.CharField(u"Название раздела", max_length=400)
	description = models.TextField(u"Описание", blank=True, null=True)
	img = models.ImageField(upload_to=get_uploaded_file_name, verbose_name=u"Картинка", blank=True, null=True)
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['created']

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = u'Раздел академии'
		verbose_name_plural = u'Раздел академии'

class Subsection(models.Model):
	title = models.CharField(u"Название подраздела", max_length=400)
	section = models.ForeignKey(Section, verbose_name=u"Раздел")
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['created']

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = u'Подраздел академии'
		verbose_name_plural = u'Подраздел академии'

class Video(models.Model):
	title = models.CharField(u"Название видео", max_length=400)
	ref_video = models.CharField(u"Ссылка на видео", max_length=400)
	subsection = models.ForeignKey(Subsection, verbose_name=u"Подраздел")
	updated = models.DateTimeField(u"Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(u"Данные созданы", auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['created']

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = u'Видео'
		verbose_name_plural = u'Видео'