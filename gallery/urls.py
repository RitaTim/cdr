from django.conf.urls import url
from .views import (
	get_albums,
	get_album,
)

urlpatterns = [
	url(r'^$', get_albums, name='gallery'),
	url(r'^(?P<symbol_code>[a-z0-9-_]+)/$', get_album, name="album_detail"),
]