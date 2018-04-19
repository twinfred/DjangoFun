from django.conf.urls import url
from . import views

urlpatterns = [
    # Render URLS
    url(r'^$', views.index),
    url(r'^books/$', views.books),
    url(r'^books/add-book$', views.add_book),
    url(r'^books/(?P<book_id>\d+)$', views.book_profile),
    url(r'^users/(?P<user_id>\d+)$', views.user_profile),
    # POST URLS
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^add$', views.add),
    url(r'^add_review/(?P<book_id>\d+)$', views.add_review),
    url(r'^delete/(?P<review_id>\d+/)(?P<user_id>\d+)$', views.delete_review),
    # Button URLS
    url(r'^logout$', views.logout),
    url(r'^clear-logged$', views.clear_logged),
    # Catch-all URL
    url(r'^', views.index),
]