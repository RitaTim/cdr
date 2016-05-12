from django.conf.urls import url, include
from .views import (
	get_news,
	get_new,
	create_new,
	update_new,
	delete_new,
)

urlpatterns = [
    url(r'^$', get_news, name='list_news'),
    url(r'^create/$', create_new),
    url(r'^edit/(?P<symbol_code>[a-z0-9-_]+)/$', update_new),
    url(r'^delete/(?P<symbol_code>[a-z0-9-_]+)/$', delete_new),
    url(r'^(?P<symbol_code>[a-z0-9-_]+)/$', get_new, name="detail"),
]