from django.contrib import admin
from .models import WhatYouGet

class WhatYouGetAdmin(admin.ModelAdmin):
	class Meta:
		model = WhatYouGet

	list_display = ['title', 'updated']
	list_filter = ['updated']
	list_editable = ['title']
	search_fields = ['title', 'description']

admin.site.register(WhatYouGet, WhatYouGetAdmin)