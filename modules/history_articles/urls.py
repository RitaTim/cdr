# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import history_page, masters_page, history_article, master_article

urlpatterns = [
	url(r'^$', history_page, name="encyclopedia"),
	url(r'^history/$', history_page, name="history"),
	url(r'^masters/$', masters_page, name="masters"),
	url(r'^history/(?P<id_article>[0-9]+)/$', history_article),
	url(r'^masters/(?P<id_article>[0-9]+)/$', master_article),
]
