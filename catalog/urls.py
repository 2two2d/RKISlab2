from django.urls import path
from . import views
from django.urls import re_path as url

urlpatterns = [
    url(r'^books/$', views.book_list, name='book_list'),
    url(r'^book/<int:pk>/$', views.book_detail, name='book_detail')
]