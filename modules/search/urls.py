# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import site_search

urlpatterns = [
	url(r'^$', site_search, name='site_search')
]
