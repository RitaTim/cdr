# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView

from slider.models import Slider
from what_you_get.models import WhatYouGet


class HomePageView(TemplateView):
	template_name = "pages/index.html"

	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data()
		context.update({
			"list_slider" : Slider.objects.all(),
			"list_what_you_get" : WhatYouGet.objects.all(),
			"unsubscribed" : self.request.session.get("unsubscribed"),
		})
		return context

home_page = HomePageView.as_view()


class RobotsPageView(TemplateView):
	template_name='robots.txt'


robots_page = RobotsPageView.as_view(content_type='text/plain')


class ErrorPageView(TemplateView):
	"""
		Дочерние вьюхи должны иметь установленное значение параметра
		status_code - возвращаемый статус ответа
	"""
	status_code = None

	def get(self, request, *args, **kwargs):
		response = super(ErrorPageView, self).get(request, *args, **kwargs)
		response.status_code = self.status_code
		return response



class Page404View(ErrorPageView):
	template_name = "404.html"
	status_code = 404

page_404 = Page404View.as_view()


class Page500View(ErrorPageView):
	template_name = "500.html"
	status_code = 500

page_500 = Page500View.as_view()
