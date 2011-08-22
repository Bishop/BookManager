from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from account.views import *

urlpatterns = patterns('',
    url(r'^$', login_required(Account.as_view()), name='account_summary'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
)
