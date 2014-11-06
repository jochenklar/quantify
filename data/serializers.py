from rest_framework import serializers

from data.models import *

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group

class FieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Field
        fields = ('name','type','unit')
        depth = 1

class RecordSerializer(serializers.ModelSerializer):

    field = FieldSerializer()

    class Meta:
        model = Record
        fields = ('field','value')
        depth = 1

class EntrySerializer(serializers.ModelSerializer):

    records = RecordSerializer()

    def save_object(self, obj, **kwargs):
        obj.user = self.context['request'].user
        obj.save()

    class Meta:
        model = Entry
        fields = ('id','date','records')
