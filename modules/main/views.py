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
