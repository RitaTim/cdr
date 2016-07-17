# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Filial

class FilialAdmin(admin.ModelAdmin):
	class Meta:
		model = Filial

	list_display = ['city', 'address', 'email', 'phone']
	list_editable = ['city', 'address', 'email', 'phone']

admin.site.register(Filial, FilialAdmin)