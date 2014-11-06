from django.db import models
from django.utils.timezone import utc
from django.contrib.auth.models import User

TYPE_CHOICES = (
    ('text','Text'),
    ('float','Float'),
    ('time','Time'),
    ('bool','Bool'),
)

class Entry(models.Model):
    user  = models.ForeignKey(User)
    date  = models.DateField()

    def __unicode__(self):
        return '%s (%s)' % (self.date,self.user.username)

    class Meta:
        ordering = ['user','-date']

class Group(models.Model):
    name  = models.CharField(max_length=512)

    def __unicode__(self):
        return self.name

class Field(models.Model):
    name  = models.CharField(max_length=512)
    group = models.ForeignKey(Group, related_name='fields')
    type  = models.CharField(max_length=8, choices=TYPE_CHOICES)
    unit  = models.CharField(max_length=8, blank=True)

    def __unicode__(self):
        return self.name

class Record(models.Model):
    entry = models.ForeignKey(Entry, related_name='records')
    field = models.ForeignKey(Field)
    value = models.CharField(max_length=512)

    def __unicode__(self):
        return '%s %s' % (unicode(self.entry),unicode(self.field))
