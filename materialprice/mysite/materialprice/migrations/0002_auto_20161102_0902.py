# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materialprice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materialprice',
            options={'verbose_name': '材料價格', 'verbose_name_plural': '材料價格'},
        ),
        migrations.RemoveField(
            model_name='materialprice',
            name='num',
        ),
        migrations.AddField(
            model_name='materialprice',
            name='weeknum',
            field=models.IntegerField(default=0, verbose_name='周'),
        ),
        migrations.AddField(
            model_name='materialprice',
            name='yearnum',
            field=models.IntegerField(default=0, verbose_name='年'),
        ),
    ]
