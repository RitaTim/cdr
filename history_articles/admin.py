from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title', 'period']
	list_filter = ['created']

	class Meta:
		model = Article

admin.site.register(Article, ArticleAdmin)
