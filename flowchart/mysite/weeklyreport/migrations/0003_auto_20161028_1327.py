# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weeklyreport', '0002_auto_20161028_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='fullname',
            field=models.CharField(max_length=32, verbose_name='員工姓名'),
        ),
    ]
