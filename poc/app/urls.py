from django.conf.urls import include, url
from django.contrib import admin

from .views import BookListView, BookListMultipleView

urlpatterns = [
    url(r'^$', BookListView.as_view(), name='book-list-single'),
    url(r'^2/$', BookListMultipleView.as_view(), name='book-list-multiple'),
]
