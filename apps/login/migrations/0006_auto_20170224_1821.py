# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20170224_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='travel',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]