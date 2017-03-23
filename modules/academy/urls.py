# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import academy_page


urlpatterns = [
	url('^$', academy_page, name="academy"),
]
