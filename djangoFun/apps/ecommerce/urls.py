from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add-to-cart/$', views.add_to_cart),
    url(r'^checkout/$', views.checkout)
]