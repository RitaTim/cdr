# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView

from citations.models import Citation
from trainers.models import Trainer
from .models import About

class AboutPageView(TemplateView):
	template_name = "pages/about.html"

	def get_context_data(self, **kwargs):
		context = super(AboutPageView, self).get_context_data()
		context.update({
			'data' : About.objects.filter().first(),
			'trainers': Trainer.objects.filter(),
			'citation': Citation.objects.filter().first(),
		})
		return context

about_page = AboutPageView.as_view()
