# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-11 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_master', '0002_auto_20180411_0958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monitorproblem',
            old_name='address',
            new_name='host',
        ),
        migrations.AlterField(
            model_name='monitorproblem',
            name='level',
            field=models.CharField(choices=[('WARNING', 'WARNING'), ('DANGER', 'DANGER')], default='WARNING', max_length=16, verbose_name='\u7ea7\u522b'),
        ),
        migrations.AlterField(
            model_name='monitorproblem',
            name='status',
            field=models.CharField(choices=[('CONFIRMED', 'CONFIRMED'), ('UNCONFIRMED', 'UNCONFIRMED')], default='UNCONFIRMED', max_length=16, verbose_name='\u72b6\u6001'),
        ),
    ]
