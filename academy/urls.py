from django.conf.urls import url
from .views import (
	show_page,
)

urlpatterns = [
	url('^$', show_page, name="academy"),
]