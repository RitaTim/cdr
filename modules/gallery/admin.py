# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Photo, Album, Category


class PhotoAdmin(admin.ModelAdmin):
	list_display = ['title']

class PhotoInline(admin.StackedInline):
	model = Photo

class AlbumAdmin(admin.ModelAdmin):
	inlines = [PhotoInline]

	list_display = ['title', 'slug']

class AlbumInline(admin.StackedInline):
	model = Album

class CategoryAdmin(admin.ModelAdmin):
	class Meta:
		model = Category

	list_display = ['title',]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
