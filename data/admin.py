from django.contrib import admin
from data.models import *

class EntryAdmin(admin.ModelAdmin):
    pass

class GroupAdmin(admin.ModelAdmin):
    pass

class FieldAdmin(admin.ModelAdmin):
    pass

class RecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Entry, EntryAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Record, RecordAdmin)
