# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160624_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='insult',
            name='pronunciation',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
