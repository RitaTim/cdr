from django.shortcuts import render

from .models import Academy, Section, Subsection, Video

def show_page(request):
	academy = Academy.objects.all()[:1].get()

	try:
		sections = Section.objects.all()
	except Section.DoesNotExists:
		sections = {}

	data = { 
		'academy' : academy,
		'sections' : sections,
	}
	return render(request, 'academy.html', data)
