# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import news_list, new_detail

urlpatterns = [
	url(r'^$', news_list, name='news_list'),
	url(r'^(?P<slug>[a-z0-9-_]+)/$', new_detail, name="new_detail"),
]
