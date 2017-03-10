# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import add_student,	new_student_form

urlpatterns = [
	url(r'^form/$', new_student_form),
	url(r'^add/$', add_student),
]
