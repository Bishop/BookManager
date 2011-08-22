from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib import databrowse
from django.views.generic.base import TemplateView
from BookManager.models import File, Publisher, Book, Edition

admin.autodiscover()

for model in [Book, Publisher, File, Edition]:
    databrowse.site.register(model)

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home_page'),
    url(r'^books/', include('BookManager.urls')),
    url(r'^databrowse/(.*)', databrowse.site.root),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )