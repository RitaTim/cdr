# -*- coding: utf-8 -*-

from django import forms

from .models import New

class NewForm(forms.ModelForm):
	class Meta:
		model = New
		fields = ['title', 'preview_text', 'detail_text']
