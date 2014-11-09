from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from data import urls

urlpatterns = patterns('',
    url(r'^$', 'quantify.views.index'),
    url(r'^csv/$', 'quantify.views.csv'),
    url(r'^form/$', 'quantify.views.form'),
    url(r'^form/(?P<date>\d\d\d\d\-\d\d\-\d\d)/$', 'quantify.views.form'),
    url(r'^login/$', 'quantify.views.login'),
    url(r'^logout/$', 'quantify.views.logout'),
    url(r'^api/', include(urls)),
    url(r'^admin/', include(admin.site.urls))
)
