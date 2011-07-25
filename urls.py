from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
from django.views.generic.edit import UpdateView
from BookManager.models import Book
from BookManager.views import BookListView, BookCreateView, BookDetail

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'books.views.home', name='home'),
    # url(r'^books/', include('books.foo.urls')),
    url(r'^books/(page(?P<page>[0-9]+)/)?$', BookListView.as_view(queryset=Book.objects.all()), name='book_list'),
    url(r'^books/add/$', BookCreateView.as_view(), name='create_book'),
    url(r'^books/update/(?P<id>[0-9]+)/$', UpdateView.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/$', BookDetail.as_view(), name='book_detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
