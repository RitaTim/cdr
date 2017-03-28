# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from .views import encyclopedia_page

urlpatterns = [
	url(r'^$', encyclopedia_page, name="encyclopedia"),
	url(r'^articles/', include("history_articles.urls")),
	url(r'^masters/', include("master.urls")),
]
