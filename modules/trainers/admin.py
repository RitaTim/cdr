# -*- coding: utf-8 -*-

from django.contrib import admin

from trainers.models import Trainer


class TrainerAdmin(admin.ModelAdmin):
	class Meta:
		model = Trainer

	list_display = ['name', 'apelido', 'status']

admin.site.register(Trainer, TrainerAdmin)
