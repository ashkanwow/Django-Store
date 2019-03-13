from django.contrib import admin
from .models import Content

class ContentAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'submite_date', 'is_published')
    fields = ('author', 'title', 'summary', 'content', 'submite_date', 'is_published' , 'photo', 'image_tag')
    readonly_fields = ('image_tag',)
    list_editable = ('is_published',)
admin.site.register(Content, ContentAdmin)
