# -*- coding: utf-8 -*-

import json

from django.contrib.sites.shortcuts import get_current_site
from django.core.context_processors import csrf
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from filials.models import Filial
from main.helpers import added_new_student

from .forms import NewStudentForm
from .models import NewStudent


def add_student(request):
	if request.method == 'POST':
		form_student = NewStudentForm(request.POST)
		if form_student.is_valid():
			student = form_student.save()

			#send message admin
			current_site = get_current_site(request)
			added_new_student(student.name, student.phone, student.filial.get_city_display(),
			                  current_site.domain)
			return render_to_response('forms/success_add_student.html', {'name' : student.name})
		else:
			return HttpResponse(
				json.dumps({
					u'error': u'Проверьте корректность введенных данных'
				}),
				content_type='application/json'
			)


class NewStudentFormView(FormView):
	form_class = NewStudentForm
	template_name = "forms/new_student.html"

	def get_context_data(self, **kwargs):
		context = super(NewStudentFormView, self).get_context_data()
		context.update({
			"filials": Filial.objects.filter()
		})
		return context


new_student_form = NewStudentFormView.as_view()
