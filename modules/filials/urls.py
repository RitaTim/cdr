# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import filials_page


urlpatterns = [
	url('^$', filials_page, name='filials'),
]
