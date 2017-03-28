# -*- coding: utf-8 -*-

from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Article
from main.helpers import get_prev_next_obj, get_random_citation


class HistoryPageView(ListView):
	model = Article
	template_name = "pages/articles.html"
	context_object_name = "articles"
	paginate_by = 5

	def get_context_data(self, **kwargs):
		context = super(HistoryPageView, self).get_context_data(**kwargs)
		context.update(get_random_citation())
		return context

articles_page = HistoryPageView.as_view()


class HistoryArticleView(DetailView):
	model = Article
	template_name = "pages/article.html"
	context_object_name = "article"

	def get_context_data(self, **kwargs):
		context = super(HistoryArticleView, self).get_context_data(**kwargs)
		context.update(get_prev_next_obj(self.object))
		context.update(get_random_citation())
		return context


article_page = HistoryArticleView.as_view()
