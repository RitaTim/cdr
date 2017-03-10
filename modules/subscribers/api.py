# -*- coding: utf-8 -*-

import json

from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http.response import HttpResponse
from django.shortcuts import redirect

from main.helpers import notify_user
from .models import Subscriber


def add_sibscribe(request):
	if request.method == 'POST':
		email = request.POST['email']

		data = {}
		if not email:
			data['error'] = u"Введите свой e-mail"
		elif Subscriber.objects.filter(email=email).exists():
			data['message'] = u"Вы уже есть в списке подписчиков"
		else:
			try:
				validate_email(email)
			except ValidationError as e:
				data['error'] = u"Введите корректный e-mail"
			else:
				Subscriber.objects.create(email=email)
				data['message'] = u"Вы подписаны на получение новостей"

				#send message to user
				current_site = get_current_site(request)
				ref_unsubscribe = "http://{}/subscribe/delete/{}/"\
								  .format(current_site.domain, email)
				notify_user(email, current_site.domain, ref_unsubscribe)
				if "unsubscribed" in request.session:
					request.session.pop('unsubscribed')

		return HttpResponse(json.dumps(data), content_type='application/json')

def delete_sibscribe(request, email=None):
	Subscriber.objects.get(email=email).delete()
	request.session["unsubscribed"] = True
	return redirect(request.META.get('HTTP_REFERER','/#form-subscribe'))
