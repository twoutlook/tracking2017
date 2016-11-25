# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materialprice', '0005_receiving'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=32, verbose_name='牌号')),
                ('pricedate', models.CharField(max_length=10, verbose_name='行情日期')),
                ('priceavg', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='平均价')),
                ('yearnum', models.IntegerField(default=0, verbose_name='年')),
                ('monthnum', models.IntegerField(default=0, verbose_name='月')),
                ('quarternum', models.IntegerField(default=0, verbose_name='季')),
            ],
            options={
                'verbose_name': '上海有色網',
                'verbose_name_plural': '上海有色網',
            },
        ),
    ]
