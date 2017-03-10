# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import NewStudent


class NewStudentAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone', 'filial']
	list_filter = ['filial']

admin.site.register(NewStudent, NewStudentAdmin)
