# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView

from .models_indexes import models_indexes

class SiteSearchTemplateView(TemplateView):
    """
        Отвечает за поиск по сайту
        Проходится по всему списку индексируемых моделей models_indexes
        и собирает данные по найденным страницам
    """
    template_name = 'search/search.html'

    def get_context_data(self, **kwargs):
        context = super(SiteSearchTemplateView, self).get_context_data()
        q = self.request.GET.get('q')
        data_indexes_pages = []
        # получаем список данных по найденым страницам
        for model in models_indexes:
            data_indexes_pages.extend(model.objects.get_indexes_pages(q))
        context.update({'data_indexes_pages': data_indexes_pages, 'q': q})
        return context


site_search = SiteSearchTemplateView.as_view()

