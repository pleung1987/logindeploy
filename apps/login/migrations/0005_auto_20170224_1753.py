# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20170222_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='travel',
            name='destination',
            field=models.ManyToManyField(related_name='travel_plan', to='login.User'),
        ),
        migrations.AddField(
            model_name='travel',
            name='traveler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User'),
        ),
    ]