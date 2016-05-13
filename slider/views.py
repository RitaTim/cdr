from .models import Slider

def get_slider(request):
	try:
		return Slider.objects.all()
	except Slider.DoesNotExists:
		return {}