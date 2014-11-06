from rest_framework import viewsets

from data.models import *
from data.serializers import *

class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.all()

class FieldViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSerializer

    def get_queryset(self):
        return Field.objects.all()

class RecordViewSet(viewsets.ModelViewSet):
    serializer_class = RecordSerializer

    def get_queryset(self):
        return Record.objects.filter(entry__user=self.request.user)
