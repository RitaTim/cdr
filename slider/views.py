from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Slider

def get_list(request):
	queryset = Slider.objects.all()
	data = {
		'list': queryset,
		'title': 'Title context',
	}
	return render(request, 'main.html', data)