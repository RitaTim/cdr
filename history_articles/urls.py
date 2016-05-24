from django.conf.urls import url
from .views import (
	show_articles,
	show_masters,
	get_master,
	get_article,
)

urlpatterns = [
	url(r'^$', show_articles),
	url(r'^history/$', show_articles),
	url(r'^masters/$', show_masters),
	url(r'^history/(?P<id_article>[0-9]+)/$', get_article),
	url(r'^masters/(?P<id_article>[0-9]+)/$', get_master),
]