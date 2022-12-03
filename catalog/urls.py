from django.urls import path
from . import views
from django.urls import re_path as url

urlpatterns = [
    url(r'^books/$', views.book_list, name='book_list'),
    url(r'^book/(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
    url(r'^authors/$', views.author_list, name='author_list'),
    url(r'^author/(?P<pk>\d+)/$', views.author_detail, name='author_detail')
]