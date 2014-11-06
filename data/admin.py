from django.contrib import admin
from data.models import *

class RecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Record, RecordAdmin)
