# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import about_page

urlpatterns = [
	url(r'^$', about_page, name='about'),
]
