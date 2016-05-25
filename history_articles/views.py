from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext

from .models import Article
from master.models import Master
from citations.models import Citation


def show_articles(request):
	articles = Article.objects.values('id', 'title', 'period')
	args = {
		'articles' : articles,
		'citation' : Citation.objects.values('master__apelido', 'master__name', 'text').order_by('?')[:1].get(),
		'section':  "history",
		'title_page':  "История капоэйры",
	}
	return render_to_response("articles.html", args, RequestContext(request))

def show_masters(request):
	articles = Master.objects.values('id', 'name', 'apelido')
	args = {
		'articles' : articles,
		'citation' : Citation.objects.values('master__apelido', 'master__name', 'text').order_by('?')[:1].get(),
		'section': "masters",
		'title_page': "История капоэйры",
	}
	return render_to_response("articles.html", args, RequestContext(request))

def get_article(request, id_article=None):
	args = {
		'article': get_object_or_404(Article, id = id_article)
	}
	return render(request, 'article.html', args)

def get_master(request, id_article=None):
	master = get_object_or_404(Master, id = id_article)
	args = {
		'article': {
			'title': master.name,
			'photo': master.photo,
			'description': master.biography,
			'apelido': master.apelido,
			'country': master.country,
			'date_b': master.date_birth,
			'date_d': master.date_death
		}
	}
	return render(request, 'article.html', args)