from django.contrib import admin

from .models import Academy, Section, Subsection, Video

class AcademyAdmin(admin.ModelAdmin):
	class Meta:
		model = Academy

class VideoAdmin(admin.ModelAdmin):
	class Meta:
		model = Video

class VideoInline(admin.StackedInline):
	model = Video

class SubsectionAdmin(admin.ModelAdmin):
	inlines = [VideoInline]

class SubsectionInline(admin.StackedInline):
	model = Subsection

class SectionAdmin(admin.ModelAdmin):
	inlines = [SubsectionInline]

admin.site.register(Academy, AcademyAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Subsection, SubsectionAdmin)
admin.site.register(Video, VideoAdmin)