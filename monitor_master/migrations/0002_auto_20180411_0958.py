# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-11 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitorhost',
            name='monitor_agent',
            field=models.CharField(choices=[('UP', 'UP'), ('DOWN', 'DOWN')], default='DOWN', max_length=5, verbose_name='Agent\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='monitorhost',
            name='port',
            field=models.CharField(max_length=32, verbose_name='\u7aef\u53e3'),
        ),
        migrations.AlterField(
            model_name='monitorhost',
            name='status',
            field=models.CharField(choices=[('UP', 'UP'), ('DOWN', 'DOWN')], default='DOWN', max_length=5, verbose_name='\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='monitornotifydetail',
            name='mode',
            field=models.CharField(choices=[('Email', 'Email'), ('SMS', 'SMS')], default='Email', max_length=10, verbose_name='\u901a\u77e5\u65b9\u5f0f'),
        ),
        migrations.AlterField(
            model_name='monitornotifydetail',
            name='status',
            field=models.CharField(choices=[('SEND', 'SEND'), ('UNSEND', 'UNSEND')], default='SEND', max_length=10, verbose_name='\u53d1\u9001\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='monitorproblem',
            name='status',
            field=models.CharField(choices=[('CONFIRMED', 'CONFIRMED'), ('UNCONFIRMED', 'UNCONFIRMED')], default='CONFIRMED', max_length=16, verbose_name='\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='monitortemplate',
            name='interval',
            field=models.CharField(choices=[('60s', '60'), ('120s', '120')], max_length=5, verbose_name='\u76d1\u63a7\u9891\u7387'),
        ),
        migrations.AlterField(
            model_name='monitortemplate',
            name='items',
            field=models.ManyToManyField(to='monitor_master.MonitorItem'),
        ),
        migrations.AlterField(
            model_name='monitortemplate',
            name='policy',
            field=models.ManyToManyField(to='monitor_master.MonitorNotifyPolicy'),
        ),
    ]
