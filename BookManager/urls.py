from django.conf.urls.defaults import patterns, url
from BookManager.models import Book
from BookManager.views import BookListView, BookCreateView, BookDetail, BookUpdateView

urlpatterns = patterns('',
    url(r'^(page(?P<page>[0-9]+)/)?$', BookListView.as_view(queryset=Book.objects.all()), name='book_list'),
    url(r'^add/$', BookCreateView.as_view(), name='create_book'),
    url(r'^update/(?P<pk>[0-9]+)/$', BookUpdateView.as_view(), name='update_book'),
    url(r'^(?P<pk>[0-9]+)/$', BookDetail.as_view(), name='book_detail'),
)
