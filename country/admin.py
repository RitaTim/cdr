from __future__ import unicode_literals
from django.contrib import admin
from .models import Country 

class CountryAdmin(admin.ModelAdmin):
	list_display = ('name', 'logo', 'updated', 'created')

admin.site.register(Country, CountryAdmin)