import datetime
from django.db import models
from django.db.models import permalink
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.db.models import Q

class Paste(models.Model):
    SYNTAX_CHOICES = {
        (0, "Plain"),
        (1, "Python"),
        (2, "HTML"),
        (3, "SQL"),
        (4, "Javascript"),
        (5, "CSS"),
    }

    content = models.TextField(max_length=10000, blank=False)
    title   = models.CharField(blank=False, max_length=30)
    syntax  = models.IntegerField(choices=SYNTAX_CHOICES, default=0)
    poster  = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="poster")
    public  = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(default=datetime.datetime.now, blank=True)
    generated_url   = models.CharField(unique=True, max_length=6, blank=False, default=get_random_string(6).lower())
    shares      = models.ManyToManyField(User, related_name="shares")
    class Meta:
        ordering = ('-timestamp',)
# Attempt at creating syntax highlighting
    def __unicode__(self):
        return "%s (%s)" % (self.title or "#%s" % self.id,
            self.get_syntax_display())

def get_paste(generated_url, user):
    query = Paste.objects.filter(generated_url=generated_url)
    if user.is_authenticated:
        return query.filter(Q(poster=user)|Q(shares=user)|Q(public=True))[0]
    else:
        return query.filter(public=True)[0]
