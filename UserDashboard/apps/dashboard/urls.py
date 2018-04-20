from django.conf.urls import url
from . import views

urlpatterns = [
    # User: User-facing pages
    url(r'^$', views.dashboard),
    url(r'^user/(?P<profile_id>\d+)$', views.user_profile),
    url(r'^user/edit$', views.edit_user),
    # Admin: User-facing pages
    url(r'^user/add$', views.add_user),
    # Admin: POST requests
    url(r'^user/(?P<user_id>\d+)/delete$', views.delete_user),
    # User: POST requests
    url(r'^update_info$', views.edit_my_info),
    url(r'^update_password$', views.edit_my_password),
    # GET requests
    # Catch-all URL
    url(r'^', views.dashboard),
]