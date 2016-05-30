from __future__ import unicode_literals
from django.contrib import admin
from .models import Citation 

class CitationAdmin(admin.ModelAdmin):
	list_display = ('text', 'master')


admin.site.register(Citation, CitationAdmin)