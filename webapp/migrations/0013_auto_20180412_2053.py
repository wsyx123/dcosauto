# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-12 12:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20180401_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitorhost',
            name='template',
        ),
        migrations.DeleteModel(
            name='MonitorNotifydetail',
        ),
        migrations.DeleteModel(
            name='MonitorNotifyPolicy',
        ),
        migrations.DeleteModel(
            name='MonitorProblem',
        ),
        migrations.DeleteModel(
            name='MonitorHost',
        ),
        migrations.DeleteModel(
            name='MonitorTemplate',
        ),
    ]
