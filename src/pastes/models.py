import datetime
from django.db import models
from django.db.models import permalink
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Paste(models.Model):
    SYNTAX_CHOICES = {
        (0, "Plain"),
        (1, "Python"),
        (2, "HTML"),
        (3, "SQL"),
        (4, "Javascript"),
        (5, "CSS"),
    }

    content     = models.CharField(max_length=10000)
    title       = models.CharField(blank=True, max_length=30)
    syntax      = models.IntegerField(choices=SYNTAX_CHOICES, default=0)
    poster      = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    public      = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(default=datetime.datetime.now, blank=True)
    generated_url   = models.CharField(db_index=True, max_length=6, blank=False, default="test")

    class Meta:
        ordering = ('-timestamp',)

    def __unicode__(self):
        return "%s (%s)" % (self.title or "#%s" % self.id,
            self.get_syntax_display())

#class PermaLink(models.Model):
#    key = models.CharField(primary_key = True, max_length = 8)
#    refersTo = models.ForeignKey(MyContentModel, unique = True)

class PasteAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title', 'poster', 'syntax', 'timestamp', 'public')
    list_filter = ('timestamp', 'syntax')

admin.site.register(Paste, PasteAdmin)
