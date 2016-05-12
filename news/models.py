from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse

from django.utils.text import slugify
from transliterate import translit, detect_language

def get_uploaded_file_name(instance, filename):
	return "news/%s" % filename

class New(models.Model):
	title = models.CharField(verbose_name="Название", max_length=100)
	slug = models.SlugField(unique=True, blank=True, null=True)
	preview_text = models.TextField(verbose_name="Описание анонса")
	detail_text = models.TextField(verbose_name="Детальное описание")
	image = models.ImageField(upload_to=get_uploaded_file_name, verbose_name="Картинка", blank=True, null=True)
	updated = models.DateTimeField(verbose_name="Данные обновлены", auto_now=True, auto_now_add=False)
	created = models.DateTimeField(verbose_name="Данные созданы", auto_now=False, auto_now_add=True)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("detail", kwargs={"symbol_code": self.slug})

	class Meta:
		ordering = ['-updated', '-created']

def pre_save_post(sender, instance, *args, **kwargs):
	if detect_language(instance.title) == 'ru':
		slug = slugify(translit(instance.title, reversed=True))
	else:
		slug = slugify(instance.title)
	exists = New.objects.filter(slug=slug).exists()
	if exists:
		slug = "%s-%s" % (slug, instance.id)

	instance.slug = slug

pre_save.connect(pre_save_post, sender=New)