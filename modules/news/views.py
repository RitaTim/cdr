# -*- coding: utf-8 -*-

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from citations.models import Citation
from .models import New

class NewListView(ListView):
	model = New
	template_name = 'pages/news.html'
	paginate_by = 5
	context_object_name = 'news'

	def get_context_data(self, **kwargs):
		context = super(NewListView, self).get_context_data()
		context.update({'citation': Citation.get_random()})
		return context


news_list = NewListView.as_view()


class NewDetailView(DetailView):
	model = New
	template_name = 'pages/new.html'

	def get_context_data(self, **kwargs):
		context = super(NewDetailView, self).get_context_data()
		context.update({'citation': Citation.get_random()})
		return context

new_detail = NewDetailView.as_view()
