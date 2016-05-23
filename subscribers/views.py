from django.shortcuts import render_to_response, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.http.response import HttpResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

import json

from .models import Subscriber
from cdr.utils import notify_user

def add_sibscribe(request):
	if request.method == 'POST':
		email = request.POST['email']

		data = {}
		if not email:
			data['error'] = "Введите свой e-mail"
		elif Subscriber.objects.filter(email=email).exists():
			data['message'] = "Вы уже есть в списке подписчиков"
		else:
			try:
				validate_email(email)
			except ValidationError as e:
				data['error'] = "Введите корректный e-mail"
			else:
				Subscriber.objects.create(email=email)
				data['message'] = "Вы подписаны на получение новостей"

				#send message to user
				current_site = get_current_site(request)
				ref_unsubscribe = "http://" + current_site.domain + "/subscribe/delete/" + email + "/"
				notify_user(email, current_site.domain, ref_unsubscribe)
				if "unsubscribed" in request.session:
					request.session.pop('unsubscribed')

		return HttpResponse(json.dumps(data), content_type='application/json')

def delete_sibscribe(request, email=None):
	Subscriber.objects.get(email=email).delete()
	data = {'message': "Вы отписались от получения новостей"}
	request.session["unsubscribed"] = True
	return redirect(request.META.get('HTTP_REFERER','/#form-subscribe'))