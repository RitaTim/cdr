# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import masters_page, master_article

urlpatterns = [
	url(r'^$', masters_page, name="masters"),
	url(r'^(?P<pk>[0-9]+)/$', master_article, name="master"),
]
