from django.db import models
from django.utils.timezone import utc
from django.contrib.auth.models import User

class Record(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()

    def __unicode__(self):
        return '%s (%s)' % (self.date,self.user.username)

    class Meta:
        ordering = ['user','-date']
