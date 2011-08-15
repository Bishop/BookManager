from django.conf.urls.defaults import patterns, url
from BookManager.views import *

urlpatterns = patterns('',
    url(r'^(page(?P<page>[0-9]+)/)?$', BookListView.as_view(), name='book_list'),
    url(r'^authors/(page(?P<page>[0-9]+)/)?$', AuthorListView.as_view(), name='author_list'),
    url(r'^author/(?P<pk>[0-9]+)/$', AuthorDetailView.as_view(), name='author_detail'),
    url(r'^add/$', BookCreateView.as_view(), name='create_book'),
    url(r'^update/(?P<pk>[0-9]+)/$', BookUpdateView.as_view(), name='update_book'),
    url(r'^(?P<pk>[0-9]+)/$', BookDetailView.as_view(), name='book_detail'),
    url(r'^(?P<pk>[0-9]+)/add_file$', BookAddFileView.as_view(), name='add_file_book'),
    url(r'^(?P<pk>[0-9]+)/add_edition$', BookAddEditionView.as_view(), name='add_edition_book'),
)
