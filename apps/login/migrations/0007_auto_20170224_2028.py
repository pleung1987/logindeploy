# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20170224_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travel',
            name='destination',
        ),
        migrations.AddField(
            model_name='travel',
            name='destination',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
