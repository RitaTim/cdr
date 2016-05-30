from django.conf.urls import url
from .views import (
	add_student,
	show_form,
)

urlpatterns = [
	url(r'^form/$', show_form),
	url(r'^add/$', add_student),
]