# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404

from citations.models import Citation
from master.models import Master
from .models import Article


class HistoryPageView(TemplateView):
	template_name = "pages/articles.html"

	def get_context_data(self, **kwargs):
		context = super(HistoryPageView, self).get_context_data()
		context.update({
			'articles' : Article.objects.values('id', 'title', 'period'),
			'citation' : Citation.objects.values(
							'master__apelido', 'master__name', 'text'
						).order_by('?').first(),
			'section':  "history",
			'title_page':  "История капоэйры",
		})
		return context

history_page = HistoryPageView.as_view()


class MastersPageView(TemplateView):
	template_name = "pages/articles.html"

	def get_context_data(self, **kwargs):
		context = super(MastersPageView, self).get_context_data()
		context.update({
			'articles': Master.objects.values('id', 'name', 'apelido'),
			'citation': Citation.objects.values(
							'master__apelido', 'master__name', 'text'
						).order_by('?').first(),
			'section': "masters",
			'title_page': "История капоэйры",
		})
		return context

masters_page = MastersPageView.as_view()


class HistoryArticleView(TemplateView):
	template_name = "pages/article.html"

	def get_context_data(self, **kwargs):
		context = super(HistoryArticleView, self).get_context_data()
		context.update({
			'article': get_object_or_404(Article, id=kwargs.get('id_article'))
		})
		return context

history_article = HistoryArticleView.as_view()


class MasterArticleView(TemplateView):
	template_name = "pages/article.html"

	def get_context_data(self, **kwargs):
		context = super(MasterArticleView, self).get_context_data()
		master = get_object_or_404(Master, id=kwargs.get('id_article'))
		context.update({
			'article': {
				'title': master.name,
				'photo': master.photo,
				'description': master.biography,
				'apelido': master.apelido,
				'country': master.country,
				'date_b': master.date_birth,
				'date_d': master.date_death
			}
		})
		return context

master_article = MasterArticleView.as_view()
