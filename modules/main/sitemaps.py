#-*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from news.models import New


class NewsSitemap(Sitemap):
	priority = 0.9
	changefreq = "daily"

	def items(self):
		return New.objects.all()

class StaticSitemap(Sitemap):
	priority = 0.8
	changefreq = 'weekly'

	def items(self):
		return ['about', 'filials', 'gallery', 'history', 'masters', 'academy', 'list_news']

	def location(self, item):
		return reverse(item)
