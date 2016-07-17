# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Master 

class MasterAdmin(admin.ModelAdmin):
	list_display = ('name', 'apelido', 'country')
	list_filter = ('country',)


admin.site.register(Master, MasterAdmin)