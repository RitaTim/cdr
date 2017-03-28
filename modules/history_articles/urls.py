# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import articles_page, article_page

urlpatterns = [
	url(r'^$', articles_page, name="articles"),
	url(r'^(?P<pk>[0-9]+)/$', article_page, name="article"),
]
