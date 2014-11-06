from django.conf.urls import patterns, include, url
from rest_framework import routers
from data.views import *

router = routers.DefaultRouter()
router.register(r'entries', EntryViewSet, base_name='entry')
router.register(r'groups', GroupViewSet, base_name='group')
router.register(r'fields', FieldViewSet, base_name='field')
router.register(r'records', RecordViewSet, base_name='record')

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
