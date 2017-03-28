# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView

from main.helpers import get_random_citation
from trainers.models import Trainer
from .models import About

class AboutPageView(TemplateView):
	template_name = "pages/about.html"

	def get_context_data(self, **kwargs):
		context = super(AboutPageView, self).get_context_data()
		context.update(get_random_citation())
		context.update({
			'data' : About.objects.filter().first(),
			'trainers': Trainer.objects.filter(),
		})
		return context

about_page = AboutPageView.as_view()
