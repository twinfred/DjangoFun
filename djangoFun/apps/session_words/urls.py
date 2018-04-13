from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add-session/$', views.add_session),
    url(r'^clear-session/$', views.clear_session)
]