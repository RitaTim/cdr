# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import TemplateView

from .models import Album, Photo


class GalleryPageView(TemplateView):
	template_name = "pages/gallery.html"

	def get_context_data(self, **kwargs):
		context = super(GalleryPageView, self).get_context_data()

		albums = Album.objects.filter()
		categories = {}
		for album in albums:
			categories.setdefault(album.category.title, [])
			categories[album.category.title].append(album)

		context.update({
			'categories' : categories
		})
		return context

gallery_page = GalleryPageView.as_view()


class AlbumPageView(TemplateView):
	template_name = "pages/album.html"

	def get_context_data(self, **kwargs):
		context = super(AlbumPageView, self).get_context_data()

		album = get_object_or_404(Album, slug=kwargs.get('symbol_code'))
		query_list = Photo.objects.filter(album=album.id)

		paginator = Paginator(query_list, 16)
		page = self.request.GET.get('page')
		try:
			photos = paginator.page(page)
		except PageNotAnInteger:
			photos = paginator.page(1)
		except EmptyPage:
			photos = paginator.page(paginator.num_pages)

		context.update({
			'album': album,
			'photos' : photos,
			'page_var': 'page',
			'paginator': paginator,
		})
		return context

album_page = AlbumPageView.as_view()
