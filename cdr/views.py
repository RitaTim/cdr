from django.shortcuts import render

from slider.views import get_slider
from what_you_get.views import get_what_you_get


def start_page(request):
	data = {
		"list_slider" : get_slider(request),
		"list_what_you_get" : get_what_you_get(request),
		"unsubscribed" : request.session.get("unsubscribed"),
	}
	return render(request, 'index.html', data)