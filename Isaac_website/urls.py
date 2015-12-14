from django.conf.urls import include, url
from django.shortcuts import render
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from . import settings

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^posts/', include('Blogs.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
