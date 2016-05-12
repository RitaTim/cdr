from modeltranslation.translator import translator, TranslationOptions
from slider.models import Slider

class SliderAdmin(TranslationOptions):
	fields = ('name', 'title_h1', 'title_h2', 'title_btn', 'href_btn',)

translator.register(Slider, SliderAdmin)