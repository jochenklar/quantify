from django.http import HttpResponseBadRequest
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from data.models import *

class RecordSerializer(serializers.ModelSerializer):
    def save_object(self, obj, **kwargs):
        obj.user = self.context['request'].user
        obj.save()

    class Meta:
        model = Record
