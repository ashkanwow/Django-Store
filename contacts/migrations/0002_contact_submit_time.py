# Generated by Django 2.1.7 on 2019-03-10 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='submit_time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
