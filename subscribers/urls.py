from django.conf.urls import url
from .views import (
	add_sibscribe,
	delete_sibscribe,
)

urlpatterns = [
	url(r'^add/$', add_sibscribe),
	url(r'^delete/(?P<email>.+)/$', delete_sibscribe),
]