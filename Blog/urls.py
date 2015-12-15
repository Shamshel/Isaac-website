from django.conf.urls import url

from Isaac_website import settings
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^page/(?P<page>[0-9]+)/$', views.post_list, name = 'post_page'),
	url(r'^post/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),

]
