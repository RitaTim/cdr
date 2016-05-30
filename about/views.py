from django.shortcuts import render
from .models import About
from trainers.models import Trainer
from citations.models import Citation

def get_about_page(request):
	query_list = About.objects.all()[0]
	trainers = Trainer.objects.all()
	citation = Citation.objects.all()[0]

	data = { 
		'data' : query_list,
		'trainers': trainers,
		'citation': citation,
	}
	return render(request, 'about.html', data)