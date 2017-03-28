# -*- coding: utf-8 -*-

"""
    models_indexes - список индексируемых моделей - моделей,
    в кот будет осуществляться поиск.

    У таких моделей должены быть:
        - менеджер, унаследованный от SearchManager модуля поиска,
          в котором должен быть определен метод get_search_qs,
          возвращающий список объектов, подходящих под поисковый запрос
        - свойство data_for_search - возвращающее данные объекта в необходимом
          для страницы поиска формате
"""
from news.models import New
from about.models import About
from gallery.models import Album
from history_articles.models import Article
from master.models import Master

models_indexes = [New, About, Album, Article, Master]
