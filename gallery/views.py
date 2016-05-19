from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Category, Album, Photo

def get_albums(request):
	catigories_data = Category.objects.all()
	albums = Album.objects.all()
	
	categories = {}
	for catigory_data in catigories_data:
		categories.update({catigory_data.title : []})

	for album in albums:
		categories[album.category.title].append(album)

	data = { 
		'categories' : categories,
	}
	return render(request, "gallery.html", data)


def get_album(request, symbol_code):
	album = Album.objects.get(slug = symbol_code)

	query_list = Photo.objects.filter(album = album.id)

	paginator = Paginator(query_list, 16)
	page = request.GET.get('page')
	try:
		photos = paginator.page(page)
	except PageNotAnInteger:
		photos = paginator.page(1)
	except EmptyPage:
		photos = paginator.page(paginator.num_pages)

	data = { 
		'album': album,
		'photos' : photos,
		'page_var': 'page',
		'paginator': paginator,
	}

	return render(request, "album.html", data)
