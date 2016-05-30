from .models import WhatYouGet

def get_what_you_get(request):
	try:
		return WhatYouGet.objects.all()
	except WhatYouGet.DoesNotExists:
		return {}