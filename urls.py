from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic.edit import CreateView, UpdateView
from BookManager.models import Book
from BookManager.views import BookListView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'books.views.home', name='home'),
    # url(r'^books/', include('books.foo.urls')),
    url(r'^books/(page(?P<page>[0-9]+)/)?$', BookListView.as_view(queryset=Book.objects.all())),
    url(r'^books/add/$', CreateView.as_view()),
    url(r'^books/update/(?P<id>[0-9]+)/$', UpdateView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
