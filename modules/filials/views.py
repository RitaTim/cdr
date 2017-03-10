# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView

from .models import Filial


class FilialsPageView(TemplateView):
	template_name = "pages/filials.html"

	def get_context_data(self, **kwargs):
		context = super(FilialsPageView, self).get_context_data()
		context.update({
			'filials' : Filial.objects.filter().order_by('id', 'city')
		})
		return context

filials_page = FilialsPageView.as_view()
