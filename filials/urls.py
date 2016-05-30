from django.conf.urls import url
from .views import (
	get_filials,
)

urlpatterns = [
	url('^$', get_filials),
]