from django.conf.urls import url
from . import views

urlpatterns = [
    # User-facing pages
    url(r'^$', views.login),
    url(r'^registration', views.registration),
    url(r'^logout', views.logout),
    # POST requests
    url(r'^login_user', views.user_login),
    url(r'^reg_user', views.user_reg),
    # GET requests
    url(r'^goodbye', views.logout_user),
    # Catch-all URL
    url(r'^', views.login),
]