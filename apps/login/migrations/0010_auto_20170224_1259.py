# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20170224_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='end',
            field=models.DateTimeField(blank=True, null=True, verbose_name=['%m/%d/%Y']),
        ),
        migrations.AlterField(
            model_name='travel',
            name='start',
            field=models.DateTimeField(blank=True, null=True, verbose_name=['%m/%d/%Y']),
        ),
    ]
