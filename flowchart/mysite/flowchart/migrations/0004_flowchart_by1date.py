# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-25 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowchart', '0003_auto_20161125_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowchart',
            name='by1date',
            field=models.DateField(blank=True, null=True, verbose_name='編制日期'),
        ),
    ]