from django.conf.urls import include, url
from .views import (
	get_list,
)

urlpatterns = [
	url(r'^get_list/', get_list),
]