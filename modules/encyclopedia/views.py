# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView


class EncyclopediaPageView(TemplateView):
	template_name = "pages/encyclopedia.html"
	url_name_article = "encyclopedia"


encyclopedia_page = EncyclopediaPageView.as_view()
