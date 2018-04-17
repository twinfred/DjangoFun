from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success/$', views.success),
    url(r'^register_account/$', views.register_account),
    url(r'^logout_user/$', views.logout),
    url(r'^login2account/$', views.login),
]