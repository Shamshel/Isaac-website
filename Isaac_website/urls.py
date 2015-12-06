from django.conf.urls import include, url
from django.shortcuts import render
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.index, name='post_list'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^posts/', include('Blogs.urls')),

]
