from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reset/$', views.reset),
    url(r'^generate/$', views.generate),
    url(r'^$', views.index),
]