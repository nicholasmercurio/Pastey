from django.contrib import admin

from .models import Paste

class PasteAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title', 'poster', 'syntax', 'timestamp', 'public', 'generated_url')
    list_filter = ('timestamp', 'syntax')

admin.site.register(Paste, PasteAdmin)
