from django.shortcuts import render

from .models import Filial

def get_filials(request):
	try:
		filials = Filial.objects.order_by('id', 'city')
	except Filial.DoesNotExists:
		filials = {}

	data = { 
		'filials' : filials,
	}
	return render(request, 'filials.html', data)
