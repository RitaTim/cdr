# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import New

class NewAdmin(admin.ModelAdmin):
	class Meta:
		model = New

	list_display = ['title', 'slug', 'preview_text', 'updated', 'created']
	list_editable = ['title', 'slug']
	list_filter = ['updated', 'created']

admin.site.register(New, NewAdmin)