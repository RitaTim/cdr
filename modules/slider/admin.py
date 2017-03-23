# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Slider


class SliderAdmin(admin.ModelAdmin):
	class Meta:
		model = Slider

	list_display = ['name', 'is_main', 'img', 'title_h1', 'title_h2', 'title_btn', 'href_btn', 'updated']
	list_filter = ['updated']
	list_editable = ['title_h1', 'title_h2', 'is_main']
	search_fields = ['title_h1', 'title_h2']

admin.site.register(Slider, SliderAdmin)
