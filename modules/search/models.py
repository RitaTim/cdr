# -*- coding: utf-8 -*-

from django.db import models


class SearchManager(models.Manager):
    """
        Менеджер для моделей, которые индексируются в поиске
    """

    def get_search_qs(self, q):
        """
            Метод возвращающий qs по поисковому запросу
        """
        raise NotImplementedError(
            "Method get_search_qs() must be implemented"
        )

    def get_indexes_pages(self, q):
        """
            Принимает на вход поисковый запрос q
            Возвращает данные по найденным страницам в виде:
            [{
                'title': <заголовок>,
                'text': <подробное описание>,
                'href': <ссылка>
            }]
            У каждой модели должно быть реализовано свойство,
            возвращающее данные объекта модели в нужном формате:
                @property
                def data_for_search(self):
                    return {
                        'title': self.title,
                        'text': self.description,
                        'href': self.get_absolute_url()
                    }
        """
        qs = self.get_search_qs(q)
        indexes_pages = []
        for album in qs:
            indexes_pages.append(album.data_for_search)
        return indexes_pages
