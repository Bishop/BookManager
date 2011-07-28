from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
from django.contrib import databrowse
from BookManager.models import File, Publisher, Book, Edition

admin.autodiscover()

for model in [Book, Publisher, File, Edition]:
    databrowse.site.register(model)

urlpatterns = patterns('',
    url(r'^books/', include('BookManager.urls')),
    url(r'^databrowse/(.*)', databrowse.site.root),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
