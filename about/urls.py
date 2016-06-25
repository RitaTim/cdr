from django.conf.urls import url
from .views import (
	get_about_page,
)

urlpatterns = [
	url(r'^$', get_about_page, name='about'),
]