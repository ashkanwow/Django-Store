from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe



class Content(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    summary = models.TextField()
    photo = models.ImageField(upload_to='blog_contents/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    submite_date = models.DateTimeField(default=datetime.now, null=True)
    content = RichTextField(null=True, blank=True)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="300" height="300" />' % (self.photo))
    image_tag.short_description = 'Image'

    def __str__(self):
         return self.title
