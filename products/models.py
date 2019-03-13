from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Product(models.Model):
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 20)
    summary = models.CharField(max_length = 200)
    photo = models.ImageField(upload_to='Products/%Y/%m/%d')
    content = RichTextField(null=True,blank=False)
    entity = models.PositiveIntegerField(range(0, 200),null=True)
    price  = models.PositiveIntegerField(null=False)
    submit_time = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
