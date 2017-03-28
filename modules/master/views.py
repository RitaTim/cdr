# -*- coding: utf-8 -*-

from django.views.generic import DetailView
from django.views.generic import ListView

from master.models import Master
from main.helpers import get_random_citation


class MastersPageView(ListView):
	model = Master
	template_name = "pages/masters.html"
	context_object_name = "masters"

	def get_context_data(self, **kwargs):
		context = super(MastersPageView, self).get_context_data(**kwargs)
		context.update(get_random_citation())
		return context

masters_page = MastersPageView.as_view()


class MasterArticleView(DetailView):
	model = Master
	template_name = "pages/master.html"
	context_object_name = "master"

	def get_context_data(self, **kwargs):
		context = super(MasterArticleView, self).get_context_data(**kwargs)
		context.update(get_random_citation())
		context.update({
			'other_masters': Master.objects.exclude(id=self.object.id)[:4]
		})
		return context


master_article = MasterArticleView.as_view()
