from django.shortcuts import render

from citations.models import Citation
from .models import Academy, Section, Subsection, Video

def show_page(request):
	try:
		sections = Section.objects.all()
	except Section.DoesNotExists:
		sections = {}

	data = {
		'sections' : sections,
		'academy' : Academy.objects.all()[:1].get(),
		'citation' : Citation.objects.values('master__apelido', 'master__name', 'text').order_by('?')[:1].get(),
	}
	return render(request, 'academy.html', data)