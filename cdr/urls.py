"""cdr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add an import:  from blog import urls as blog_urls
	2. Import the include() function: from django.conf.urls import url, include
	3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from .views import start_page
from .sitemaps import StaticSitemap, NewsSitemap

sitemaps = {
	'static': StaticSitemap,
	'news' : NewsSitemap,
}

urlpatterns = [
	url(r'^$', start_page),
	url(r'^admin/', admin.site.urls),
	url(r'^news/', include("news.urls")),
	url(r'^filials/', include("filials.urls")),
	url(r'^gallery/', include("gallery.urls")),
	url(r'^about/', include("about.urls")),
	url(r'^new-student/', include("new_student.urls")),
	url(r'^subscribe/', include("subscribers.urls")),
	url(r'^academy/', include("academy.urls")),
	url(r'^encyclopedia/', include("history_articles.urls")),
	url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)