from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<user_id>\d+)/edit$', views.edit),
    url(r'^update/$', views.update),
    url(r'^new/$', views.new),
    url(r'^create/$', views.create),
    url(r'^(?P<user_id>\d+)/destroy/$', views.destroy),
    url(r'^(?P<user_id>\d+)/$', views.show),
    url(r'^$', views.index),
]