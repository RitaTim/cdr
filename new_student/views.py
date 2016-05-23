from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.sites.shortcuts import get_current_site

import json

from .forms import NewStudentForm
from .models import NewStudent
from filials.models import Filial
from cdr.utils import added_new_student

def add_student(request):
	if request.method == 'POST':
		name = request.POST['name']
		phone = request.POST['phone']
		id_filial = request.POST['filial']
		filial = Filial.objects.get(id=id_filial)

		data = {}
		form_student = NewStudentForm(request.POST)
		if form_student.is_valid():
			student = NewStudent.objects.create(
				name = name,
				phone = phone,
				filial = filial
			)

			#send message admin
			current_site = get_current_site(request)
			added_new_student(name, phone, filial.get_city_display() , current_site.domain)

			return render_to_response('success_add_student.html', {'name' : name})
		else:
			data['error'] = 'Проверьте корректность введенных данных'

		return HttpResponse(json.dumps(data), content_type='application/json')


def show_form(request):
	args = {}
	args.update(csrf(request))
	args ['form'] =  NewStudentForm()
	args['filials'] = Filial.objects.all()
	return render_to_response('form_add_student.html', args)