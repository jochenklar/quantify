from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from data import urls

urlpatterns = patterns('',
    url(r'^$', 'quantify.views.index'),
    url(r'^login/$', 'quantify.views.login'),
    url(r'^logout/$', 'quantify.views.logout'),
    url(r'^api/', include(urls)),
    url(r'^admin/', include(admin.site.urls))
)
