# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-31 03:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_imageregistry'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u540d\u79f0')),
                ('address', models.CharField(max_length=32, unique=True, verbose_name='IP\u5730\u5740')),
                ('status', models.CharField(default='enabled', max_length=15, verbose_name='\u72b6\u6001')),
                ('monitor_agent', models.CharField(default='down', max_length=5, verbose_name='Agent\u72b6\u6001')),
            ],
        ),
        migrations.CreateModel(
            name='MonitorTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='\u540d\u79f0')),
                ('cpu', models.CharField(blank=True, max_length=64, null=True, verbose_name='cpu')),
                ('memory', models.CharField(blank=True, max_length=64, null=True, verbose_name='memory')),
                ('disk', models.CharField(blank=True, max_length=225, null=True, verbose_name='disk')),
                ('network', models.CharField(blank=True, max_length=64, null=True, verbose_name='network')),
            ],
        ),
        migrations.AlterField(
            model_name='imageregistry',
            name='address',
            field=models.CharField(max_length=32, unique=True, verbose_name='IP\u5730\u5740'),
        ),
        migrations.AddField(
            model_name='monitorhost',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.MonitorTemplate', verbose_name='\u6a21\u7248'),
        ),
    ]
