# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-23 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_auto_20170123_1729'),
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='author.Author'),
            preserve_default=False,
        ),
    ]
