from django.contrib import admin

# Register your models here.
from .models import Paste
#class PermaLink(models.Model):
#    key = models.CharField(primary_key = True, max_length = 8)
#    refersTo = models.ForeignKey(MyContentModel, unique = True)

class PasteAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title', 'poster', 'syntax', 'timestamp', 'public', 'generated_url')
    list_filter = ('timestamp', 'syntax')

admin.site.register(Paste, PasteAdmin)
