# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView

from citations.models import Citation
from .models import Academy, Section

class AcademyPageView(TemplateView):
	template_name = "pages/academy.html"

	def get_context_data(self, **kwargs):
		context = super(AcademyPageView, self).get_context_data()
		context.update({
			'sections' : Section.objects.filter(),
			'academy' : Academy.objects.filter().first(),
			'citation' : Citation.objects.values('master__apelido', 'master__name', 'text').order_by('?').first(),
		})
		return context

academy_page = AcademyPageView.as_view()
