from __future__ import unicode_literals
from django.contrib import admin
from .models import About 

class AboutAdmin(admin.ModelAdmin):
	list_display = ('title', 'text')

admin.site.register(About, AboutAdmin)