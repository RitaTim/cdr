# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
	url(r'^admin/', admin.site.urls),

	url(r'^', include("main.urls")),
	url(r'^news/', include("news.urls")),
	url(r'^filials/', include("filials.urls")),
	url(r'^gallery/', include("gallery.urls")),
	url(r'^about/', include("about.urls")),
	url(r'^new-student/', include("new_student.urls")),
	url(r'^subscribe/', include("subscribers.urls")),
	url(r'^academy/', include("academy.urls")),
	url(r'^encyclopedia/', include("history_articles.urls")),
]

handler404 = 'main.views.page_404'
handler500 = 'main.views.page_500'

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
