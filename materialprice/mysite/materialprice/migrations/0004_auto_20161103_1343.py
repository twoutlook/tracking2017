# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 05:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materialprice', '0003_purchaseorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='podate',
            field=models.DateField(verbose_name='订单日期'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='unit',
            field=models.CharField(default='KG', max_length=32, verbose_name='单位'),
        ),
    ]
