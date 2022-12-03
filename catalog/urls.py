from django.urls import path
from . import views
from django.urls import re_path as url

urlpatterns = [
    url(r'^books/$', views.BookList.as_view(), name='book_list'),
    url(r'^book/(?P<pk>\d+)/$', views.BookDetail.as_view(), name='book_detail'),
    url(r'^books/(?P<field>\w+)=(?P<property>[\w ]+)/$', views.BookFind.as_view(), name='book_find'),
    url(r'^authors/$', views.AuthorList.as_view(), name='author_list'),
    url(r'^author/(?P<pk>\d+)/$', views.AuthorDetail.as_view(), name='author_detail'),
]