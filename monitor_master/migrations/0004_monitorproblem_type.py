# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-11 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_master', '0003_auto_20180411_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitorproblem',
            name='type',
            field=models.CharField(default='cpu', max_length=15, verbose_name='\u7c7b\u578b'),
            preserve_default=False,
        ),
    ]
