from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from citations.models import Citation
from .forms import NewForm
from .models import New

def get_news(request):
	query_list = New.objects.all()
	paginator = Paginator(query_list, 5)

	page = request.GET.get('page')
	try:
		query = paginator.page(page)
	except PageNotAnInteger:
		query = paginator.page(1)
	except EmptyPage:
		query = paginator.page(paginator.num_pages)

	data = { 
		'news' : query,
		'page_var': 'page',
		'paginator': paginator,
		'citation': Citation.objects.values('master__apelido', 'master__name', 'text').order_by('?')[:1].get(),
	}
	return render(request, 'news.html', data)

def get_new(request, symbol_code=None):
	data = {
		'new': get_object_or_404(New, slug=symbol_code),
		'citation': Citation.objects.values('master__apelido', 'master__name', 'text').order_by('?')[:1].get(),
	}
	return render(request, 'new.html', data)

def create_new(request):
	form = NewForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'New created')
		return HttpResponseRedirect(instance.get_absolute_url())

	data = {
		'form': form,
	}
	return render(request, 'new_form.html', data)

def update_new(request, symbol_code=None):
	instance = get_object_or_404(New, slug=symbol_code)
	form = NewForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, 'New updated')
		return HttpResponseRedirect(instance.get_absolute_url())

	data = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, 'new_update.html', data)

def delete_new(request, symbol_code=None):
	instance = get_object_or_404(New, slug=symbol_code)
	instance.delete()
	messages.success(request, 'New deleted')
	return redirect("list_news")