# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap

from .views import home_page, robots_page
from .sitemaps import StaticSitemap, NewsSitemap, ArticlesSitemap, MastersSitemap

sitemaps = {
	'static': StaticSitemap,
	'news' : NewsSitemap,
	'articles': ArticlesSitemap,
	'masters': MastersSitemap
}

urlpatterns = [
	url(r'^$', home_page, name='index'),
	url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	url(r'^robots\.txt$', robots_page, name='robots')
]
