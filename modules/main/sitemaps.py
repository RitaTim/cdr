#-*- coding: utf-8 -*-

from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from news.models import New
from history_articles.models import Article
from master.models import Master


class NewsSitemap(Sitemap):
	priority = 0.9
	changefreq = "daily"

	def items(self):
		return New.objects.all()


class ArticlesSitemap(Sitemap):
	priority = 0.9
	changefreq = "daily"

	def items(self):
		return Article.objects.all()


class MastersSitemap(Sitemap):
	priority = 0.9
	changefreq = "daily"

	def items(self):
		return Master.objects.all()


class StaticSitemap(Sitemap):
	priority = 0.8
	changefreq = 'weekly'

	def items(self):
		return ['about', 'filials', 'gallery', 'articles', 'masters',
		        'academy', 'news_list']

	def location(self, item):
		return reverse(item)
