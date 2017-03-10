# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import gallery_page, album_page

urlpatterns = [
	url(r'^$', gallery_page, name='gallery'),
	url(r'^(?P<symbol_code>[a-z0-9-_]+)/$', album_page, name="album_detail"),
]
