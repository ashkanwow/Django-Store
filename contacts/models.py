from django import forms
from django.db import models
from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length = 30)
    topic = models.CharField(max_length=200)
    comment = models.TextField()
    submit_time = models.TimeField(default=datetime.now)
    def __str__(self):
        return self.name
  

