from django.db import models
from django.utils.timezone import utc
from django.contrib.auth.models import User

TYPE_CHOICES = (
    ('text','Text'),
    ('float','Float'),
    ('time','Time'),
    ('bool','Bool'),
    ('time','Time'),
)

class Entry(models.Model):
    user  = models.ForeignKey(User)
    date  = models.DateField()

    def __unicode__(self):
        return '%s (%s)' % (self.date,self.user.username)

    class Meta:
        ordering = ['user','-date']

class Group(models.Model):
    user  = models.ForeignKey(User)
    name  = models.CharField(max_length=512)

    def __unicode__(self):
        return '%s, %s' % (self.user, self.name)

    class Meta:
        ordering = ['user','name']

class Field(models.Model):
    name  = models.CharField(max_length=512)
    group = models.ForeignKey(Group, related_name='fields')
    type  = models.CharField(max_length=8, choices=TYPE_CHOICES)
    unit  = models.CharField(max_length=8, blank=True)

    def __unicode__(self):
        return '%s, %s, %s' % (self.group.user,self.group.name,self.name)

    class Meta:
        ordering = ['group','name']

class Record(models.Model):
    entry = models.ForeignKey(Entry, related_name='records')
    field = models.ForeignKey(Field, related_name='records')
    value = models.CharField(max_length=512)

    def __unicode__(self):
        return '%s, %s, %s' % (self.entry.date,self.entry.user,self.field.name)

    class Meta:
        ordering = ['entry','field']
