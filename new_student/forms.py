from django import forms

from .models import NewStudent

class NewStudentForm(forms.ModelForm):
	class Meta:
		model = NewStudent
		fields = ['name', 'phone', 'filial']