# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20170224_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='end',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='start',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]