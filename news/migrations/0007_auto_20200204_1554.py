# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-04 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20200204_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='news.Tags'),
        ),
    ]
